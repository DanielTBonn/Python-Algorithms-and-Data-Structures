from BinaryTree import BinaryTree
from StackClass import Stack
import operator

def build_parse_tree(fp_expr):
    fp_list = fp_expr_split(fp_expr)
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree
    
    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in ["+", "-", "*", "/", "|", "&", "!"]:
            if i == "!":
                parent = p_stack.pop()
                current_tree = parent
                current_tree.left_child = None
            current_tree.key = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child            
        elif i.isdigit():
            current_tree.key= int(i)
            parent = p_stack.pop()
            current_tree = parent

        elif i == ")":
              current_tree = p_stack.pop()
        else:
              raise ValueError(f"Unknown operator '{i}'")

    return expr_tree

def fp_expr_split(fp_expr):
    fp_list = []
    res = ''
    
    for item in fp_expr:
        if item.isdigit():
            res += item
        elif item == ' ':
            pass
        else:
            if res.isdigit():
                fp_list.append(res)
                res = ''
            fp_list.append(item)
    
    return fp_list

def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)

def print_exp(tree):
    result = ""
    if tree:
        result += print_exp(tree.get_left_child())
        result = result + str(tree.key)
        result = result + print_exp(tree.get_right_child())

        if tree.key in ["+", "-", "*", "/", "|", "&", "!"]:
            result = '(' + result + ')'
 
    return result
        
def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "|": operator.or_,
        "&": operator.and_,
        "!": operator.not_,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.key]
        return fn(evaluate(left_child), evaluate(right_child))
    elif right_child:
        fn = operators[parse_tree.key]
        return fn(evaluate(right_child))
    else:
        return parse_tree.key

def main():
    pt = build_parse_tree("(!(10*3))")
    print(print_exp(pt))  
    postorder(pt)
    print(evaluate(pt))

if __name__ == '__main__':
    main()
