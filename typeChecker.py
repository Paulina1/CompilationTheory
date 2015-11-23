class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

class NodeVisitor(object): #oryginalna ze stronki z dokumentacją

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for field, value in iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)


    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self)
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op;
        # ...
        #

    def visit_Const(self, node):

    def visit_Declaraions(self, node):
    def visit_Declaration(self, node):
    def visit_Instructions(self, node):
    def visit_ReturnInstr(self, node):
    def visit_PrintInstr(self, node):
    def visit_Inits(self, node):
    def visit_Init(self, node):
    def visit_AssignmentInstruction(self, node):
    def visit_ChoiceInstr(self, node):
    def visit_WhileIstr(self, node):
    def visit_RepeatInstr(self, node):
    def visit_ContinueInstr(self, node):
    def visit_BreakInstruction(self, node):
    def visit_CompoundInstruction(self, node):
    def visit_CastFunction(self, node):
    def visit_ExprInBrackets(self, node):
    def visit_ExpressionList(self, node):
    def visit_FunctionList(self, node):
    def visit_Function(self, node):
    def visit_Arguments(self, node):
    def visit_Argument(self, node):
    def visit_Block(self, node):
    def visit_Blocks(self, node):
#    def visit_RelExpr(self, node):
#        type1 = self.visit(node.left)     # type1 = node.left.accept(self)
#        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
#        # ...
#        #
#
#    def visit_Integer(self, node):
#        return 'int'
#
#    #def visit_Float(self, node):
