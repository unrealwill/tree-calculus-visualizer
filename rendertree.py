import graphviz


colormap ={"a":"blue","b":"yellow","c":"green","u":"magenta","v":"orange"}

def create_binarytree_graph(data):
    """
    Transforms an unnamed nested tuple into a Graphviz graph without labels.
    Only works when tuple have less than 2 children
    Args:
        data (tuple): An unnamed nested tuple representing the graph structure.

    Returns:
        graphviz.Digraph: A Graphviz directed graph object.
    """
    graph = graphviz.Digraph(format='png')

    def traverse(node, idparent, id):   
        if isinstance(node, tuple):
            graph.node(str(id),label="")
            for idx in range(len(node)):
                child = node[idx]
                idxchild = 2*id+idx+1
                graph.edge(str(id), str(idxchild) )
                traverse(child, id, idxchild )
        else:      
            if isinstance(node, str):
                 graph.node(str(id),label=node,style="filled",color=colormap[node] )
            else:
                graph.node(str(id),label="",style="filled",color="red")

    traverse(data, 0, 0)
    return graph

t=0 #value is not used
a = "a"
b = "b"
c = "c"
u = "u"
v = "v"

#graph_data =  (((t,(t,(t,t))),(t,(t,t))),t )
rule1input =  (((t, t),a), b)
create_binarytree_graph(rule1input).render('rule1-input', view=False)
rule1output = a
create_binarytree_graph(rule1output).render('rule1-output', view=False)

rule2input =  (((t, (t,a)),b), c )
create_binarytree_graph(rule2input).render('rule2-input', view=False)
rule2output =  ((a,c),(b,c))
create_binarytree_graph(rule2output).render('rule2-output', view=False)

rule3ainput = (((t,((t,a),b)),c),t)
create_binarytree_graph(rule3ainput).render('rule3a-input', view=False)
rule3aoutput = a
create_binarytree_graph(rule3aoutput).render('rule3a-output', view=False)

rule3binput = (((t,((t,a),b)),c),(t,u))
create_binarytree_graph(rule3binput).render('rule3b-input', view=False)
rule3boutput = (b, u)
create_binarytree_graph(rule3boutput).render('rule3b-output', view=False)

rule3cinput = (((t,((t,a),b)),c),((t,u),v))
create_binarytree_graph(rule3cinput).render('rule3c-input', view=False)
rule3coutput = ((c, u),v)
create_binarytree_graph(rule3coutput).render('rule3c-output', view=False)