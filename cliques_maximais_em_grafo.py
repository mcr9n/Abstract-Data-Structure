class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __repr__(self):
        return self.name

rs = Node('rs')
sc = Node('sc')
pr = Node('pr')
sp = Node('sp')
ms = Node('ms')
rj = Node('rj')
es = Node('es')
mg = Node('mg')
go = Node('go')
mt = Node('mt')
ba = Node('ba')
se = Node('se')
al = Node('al')
pe = Node('pe')
pb = Node('pb')
rn = Node('rn')
ce = Node('ce')
pi = Node('pi')
to = Node('to')
pa = Node('pa')
ma = Node('ma')
ap = Node('ap')
rr = Node('rr')
am = Node('am')
ro = Node('ro')
ac = Node('ac')



rs.neighbors = [sc]
sc.neighbors = [pr, rs]
pr.neighbors = [ms,sp,sc]
sp.neighbors = [ms,mg,rj,pr]
ms.neighbors = [mt,go,mg,sp,pr]
rj.neighbors = [es,sp,mg]
es.neighbors = [ba,mg,rj]
mg.neighbors = [go,ba,es,rj,sp,ms]
go.neighbors = [mt, to, ba, mg, ms]
mt.neighbors = [am, ro, pa, go]
ba.neighbors = [to, pi, pe, al, se, es, mg, go]
se.neighbors = [al, ba]
al.neighbors = [pe, ce, ba]
pe.neighbors = [pi, ce, pb, al, ba]
pb.neighbors = [pe, ce, rn]
rn.neighbors = [ce, pb]
ce.neighbors = [pi, rn, pb, pe]
pi.neighbors = [ma, to, ce, ba, pe]
to.neighbors = [mt, pa, ma, go, pi, ce]
pa.neighbors = [am, rr, mt, ap, ma, to]
ma.neighbors = [pa, to, pi, ce]
ap.neighbors = [pa]
rr.neighbors = [am, pa]
am.neighbors = [ac, ro, mt, pa, rr]
ro.neighbors = [ac, am]
ac.neighbors = [am, ro]

all_nodes = [rs, sc, pr, sp, ms, rj, es, ms, go, mt, ba, se, al, pe, pb, rn, ce, pi, to, pa, ma, ap, rr, am, ro, ac]


def find_cliques(potential_clique=[], remaining_nodes=[], skip_nodes=[], depth=0):

    if len(remaining_nodes) == 0 and len(skip_nodes) == 0:
        print(potential_clique)
        return 1

    found_cliques = 0
    for node in remaining_nodes:

        # Try adding the node to the current potential_clique to see if we can make it work.
        new_potential_clique = potential_clique + [node]
        new_remaining_nodes = [n for n in remaining_nodes if n in node.neighbors]
        new_skip_list = [n for n in skip_nodes if n in node.neighbors]
        found_cliques += find_cliques(new_potential_clique, new_remaining_nodes, new_skip_list, depth + 1)

        # We're done considering this node.  If there was a way to form a clique with it, we
        # already discovered its maximal clique in the recursive call above.  So, go ahead
        # and remove it from the list of remaining nodes and add it to the skip list.
        remaining_nodes.remove(node)
        skip_nodes.append(node)
    return found_cliques

find_cliques(remaining_nodes=all_nodes)

        



    
