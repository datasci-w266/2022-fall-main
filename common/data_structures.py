from __future__ import print_function, unicode_literals

import sys
import numpy as np

##
# From nltk.compat
from six import string_types, text_type
PY3 = sys.version_info[0] == 3
def unicode_repr(obj):
    """
    For classes that was fixed with @python_2_unicode_compatible
    ``unicode_repr`` returns ``obj.unicode_repr()``; for unicode strings
    the result is returned without "u" letter (to make output the
    same under Python 2.x and Python 3.x); for other variables
    it is the same as ``repr``.
    """
    if PY3:
        return repr(obj)

    # Python 2.x
    if hasattr(obj, 'unicode_repr'):
        return obj.unicode_repr()

    if isinstance(obj, text_type):
        return repr(obj)[1:]  # strip "u" letter from output

    return repr(obj)

##
# Lightweight replacement for nltk.tree.ProbabilisticTree
class ProbabilisticTree(object):
    def __init__(self, label, children, logprob=-np.inf):
        self._label = label
        self._children = children
        self._logprob = logprob

    def label(self):
        return self._label

    def logprob(self):
        return self._logprob

    def leaves(self):
        ret = []
        self._find_leaves(ret)
        return ret

    def _find_leaves(self, ret):
        # In-order traversal of leaves
        if len(self) == 0:
            ret.append(self.label())
            return
        for child in self:
            if isinstance(child, ProbabilisticTree):
                child._find_leaves(ret)
            else:
                ret.append(child)

    def __len__(self):
        return len(self._children)

    def __getitem__(self, index):
        return self._children[index]

    def __iter__(self):
        return self._children.__iter__()

    def _repr_html_(self):
        import treeviz
        return treeviz.render_tree(self, title=treeviz.make_title(self), format='png')

    ##
    # Pretty-printing code copied from nltk.tree.Tree
    def __str__(self):
        return self.pformat()

    def pprint(self, **kwargs):
        """
        Print a string representation of this Tree to 'stream'
        """

        if "stream" in kwargs:
            stream = kwargs["stream"]
            del kwargs["stream"]
        else:
            stream = None
        print(self.pformat(**kwargs), file=stream)

    def pformat(self, margin=70, indent=0, nodesep='', parens='()', quotes=False):
        """
        :return: A pretty-printed string representation of this tree.
        :rtype: str
        :param margin: The right margin at which to do line-wrapping.
        :type margin: int
        :param indent: The indentation level at which printing
            begins.  This number is used to decide how far to indent
            subsequent lines.
        :type indent: int
        :param nodesep: A string that is used to separate the node
            from the children.  E.g., the default value ``':'`` gives
            trees like ``(S: (NP: I) (VP: (V: saw) (NP: it)))``.
        """

        # Try writing it on one line.
        s = self._pformat_flat(nodesep, parens, quotes)
        if len(s) + indent < margin:
            return s

        # If it doesn't fit on one line, then write it on multi-lines.
        if isinstance(self._label, string_types):
            s = '%s%s%s' % (parens[0], self._label, nodesep)
        else:
            s = '%s%s%s' % (parens[0], unicode_repr(self._label), nodesep)
        for child in self:
            if isinstance(child, ProbabilisticTree):
                s += '\n'+' '*(indent+2)+child.pformat(margin, indent+2,
                                                  nodesep, parens, quotes)
            elif isinstance(child, tuple):
                s += '\n'+' '*(indent+2)+ "/".join(child)
            elif isinstance(child, string_types) and not quotes:
                s += '\n'+' '*(indent+2)+ '%s' % child
            else:
                s += '\n'+' '*(indent+2)+ unicode_repr(child)
        return s+parens[1]
    
    def _pformat_flat(self, nodesep, parens, quotes):
        childstrs = []
        for child in self:
            if isinstance(child, ProbabilisticTree):
                childstrs.append(child._pformat_flat(nodesep, parens, quotes))
            elif isinstance(child, tuple):
                childstrs.append("/".join(child))
            elif isinstance(child, string_types) and not quotes:
                childstrs.append('%s' % child)
            else:
                childstrs.append(unicode_repr(child))
        if isinstance(self._label, string_types):
            return '%s%s%s %s%s' % (parens[0], self._label, nodesep,
                                    " ".join(childstrs), parens[1])
        else:
            return '%s%s%s %s%s' % (parens[0], unicode_repr(self._label), nodesep,
                                    " ".join(childstrs), parens[1])
