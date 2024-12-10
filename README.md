# tree-calculus-visualizer
render the trees corresponding to the rules of tree calculus https://treecalcul.us/

The red node are the leaf (terminal), the white nodes correspond to the internal nodes of the tree, the other colored node correspond to the placeholder for subtrees.

Given a binary tree we pattern match it, and transform it according to the following visual rules : 

Tree calculus computation consist in applying the transforms to the binary tree as much as we can.
A computation in tree calculus is done when we can no longer find a matching pattern.

# Rule 1 :
t t a b -> a

![rule1input](rule1-input.png) -> ![rule1output](rule1-output.png) 

# Rule 2 :
t (t a) b c -> a c (b c)

![rule2input](rule2-input.png) -> ![rule2output](rule2-output.png) 

# Rule 3 a :
t (t a b) c t -> a

![rule3ainput](rule3a-input.png) -> ![rule3aoutput](rule3a-output.png) 

# Rule 3 b :
t (t a b) c (t u) -> b u

![rule3binput](rule3b-input.png) -> ![rule3boutput](rule3b-output.png) 

# Rule 3 c :
t (t a b) c (t u v) -> c u v

![rule3cinput](rule3c-input.png) -> ![rule3coutput](rule3c-output.png) 


# How it's made :

You need to  ```pip3 install graphviz ``` 
I parsed manually the left associativity to make the parenthesis explicit (to the best of my ability, please excuse any unfortunate mistake).
And I used  ```python3 rendertree.py```  which transform nested tuple into graphviz  graph that are rendered to image.

