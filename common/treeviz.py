from __future__ import print_function
from __future__ import division

import nltk
import graphviz as gv

def monkey_patch(tree_class, node_style_fn=None, format='svg', graph_attr={}):
	def render_fn(tree):
	    return render_tree(tree, title=make_title(tree),
						   node_style_fn=node_style_fn,
						   format=format, **graph_attr)
	tree_class._repr_png_ = lambda _: None
	tree_class._repr_html_ = render_fn

def clean_kw(kw):
    return {k:str(v) for k,v in kw.items()}

class Graph(object):
    """Yet another GraphViz wrapper, but I control it this time goddamnit.

    This exists because Python GraphViz bindings are all terrible and keep
    breaking, so its advantageous to have a high-level wrapper that can do what
    we want and make calls to low-level rendering code.

    Implement the build() function to interface with an actual GraphViz
    backend such as pydotplus or graphviz.
    """
    def __init__(self, name, **attr):
        self._name = name
        self._attr = attr
        self._subgraphs = []
        self._node_map = {}
        self._edge_map = {}

    def add_graph_attr(self, key, value):
        self._attr[key] = value

    def add_subgraph(self, sg):
        self._subgraphs.append(sg)

    def add_node(self, name, label=None, **kw):
        name = str(name)
        assert(name not in self._node_map)
        self._node_map[name] = (label, kw)

    def add_edge(self, start, end, **kw):
        key = (str(start), str(end))
        assert(key not in self._edge_map)
        self._edge_map[key] = kw

    def build(self):
        """Build a graphviz Digraph object."""
        G = gv.Digraph(self._name, graph_attr=clean_kw(self._attr))
        for sg in self._subgraphs:
            G.subgraph(sg.build())
        for name, (label, kw) in self._node_map.items():
            G.node(name, label, **clean_kw(kw))
        for key, kw in self._edge_map.items():
            G.edge(*key, **clean_kw(kw))
        return G

    def render(self, format='png'):
        G = self.build()
        G.format = format
        if (format == 'png'):
            return G.pipe()
        elif (format == "svg"):
            return G.pipe().decode('utf-8')
        else:
            raise ValueError("Unrecognized rendering format {:s}".format(format))


from . import data_structures

def is_tree(t):
    return (isinstance(t, nltk.tree.Tree)
            or isinstance(t, data_structures.ProbabilisticTree))

def _tree_to_graph(t, G, ids, token_ids, parent=None, node_style_fn=None):
    ids.append(ids[-1] + 1 if ids else 0)
    this_id = ids[-1]
    if parent is not None:
        G.add_edge(parent, this_id)
    style = (node_style_fn(t) if node_style_fn else {})
    if is_tree(t):
        label = str(t.label())
        tooltip = '"%s"' % t.pformat(margin=30)
        G.add_node(this_id, label=label, tooltip=tooltip, **style)
        for st in t[:]:
            _tree_to_graph(st, G, ids, token_ids, parent=this_id,
                           node_style_fn=node_style_fn)
    else:
        label = str(t)
        G.add_node(this_id, label=label, tooltip=label, shape='box', **style)
        token_ids.append(this_id)


def tree_to_graph(t, G=None, node_style_fn=None):
    G = G or Graph("tree")
    ids = []
    token_ids = []
    _tree_to_graph(t, G, ids, token_ids, parent=None,
                   node_style_fn=node_style_fn)

    # Make token subgraph to constrain layout
    sg = Graph(name="tokens", rank="same")
    for token_id in token_ids:
        sg.add_node(token_id)
    G.add_subgraph(sg)
    # Add token-token edges to preserve sequence
    # Token ids should be sequential, due to left-right traversal.
    for i in range(1, len(token_ids)):
        G.add_edge(token_ids[i-1], token_ids[i],
                   arrowsize=0, penwidth=1, color="#CCCCCC")

    return G

def embed_png_in_html(raw_data):
    import base64
    encoded_data = base64.b64encode(raw_data)
    return "<img src=\"data:image/png;base64," + encoded_data.decode("ascii") + "\">"

def render_graph(G, format='png', title=None, **graph_attr):
    from IPython.display import display, Image, SVG, HTML
    import base64
    for (k, v) in graph_attr.items():
        G.add_graph_attr(k, v)
    ret = []
    if title:
        ret.append("<h4>" + title + "</h4>")
    if format == 'svg':
        ret.append(G.render(format='svg'))
    elif format == 'png':
        png_data = G.render(format='png')
        ret.append(embed_png_in_html(png_data))
    else:
        raise ValueError("Invalid render format " + format)
    return "\n".join(ret)

def make_title(t):
    s = " ".join(t.leaves())
    if hasattr(t, 'logprob'):
        return s + "  (score = %.03f)" % t.logprob()
    return s

def render_tree(t, node_style_fn=None, **kw):
    return render_graph(tree_to_graph(t, None, node_style_fn), **kw)
