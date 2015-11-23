ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

ttype['*']['string']['int'] = 'string'

ttype['&']['int']['int'] = 'int'
ttype['^']['int']['int'] = 'int'
ttype['|']['int']['int'] = 'int'
ttype['AND']['int']['int'] = 'int'
ttype['OR']['int']['int'] = 'int'
ttype['SHL']['int']['int'] = 'int'
ttype['SHR']['int']['int'] = 'int'

ttype['+']['float']['int'] = 'float'
ttype['+']['int']['float'] = 'float'
ttype['+']['float']['float'] = 'float'
ttype['+']['int']['int'] = 'int'
ttype['-']['float']['int'] = 'float'
ttype['-']['int']['float'] = 'float'
ttype['-']['float']['float'] = 'float'
ttype['-']['int']['int'] = 'int'
ttype['*']['float']['int'] = 'float'
ttype['*']['int']['float'] = 'float'
ttype['*']['float']['float'] = 'float'
ttype['*']['int']['int'] = 'int'
ttype['/']['float']['int'] = 'float'
ttype['/']['int']['float'] = 'float'
ttype['/']['float']['float'] = 'float'
ttype['/']['int']['int'] = 'int'

ttype['>']['int']['int'] = 'int'
ttype['<']['int']['int'] = 'int'
ttype['LE']['int']['int'] = 'int'
ttype['GE']['int']['int'] = 'int'
ttype['EQ']['int']['int'] = 'int'
ttype['NEQ']['int']['int'] = 'int'
ttype['>']['int']['float'] = 'int'
ttype['<']['int']['float'] = 'int'
ttype['LE']['int']['float'] = 'int'
ttype['GE']['int']['float'] = 'int'
ttype['EQ']['int']['float'] = 'int'
ttype['NEQ']['int']['float'] = 'int'
ttype['>']['float']['int'] = 'int'
ttype['<']['float']['int'] = 'int'
ttype['LE']['float']['int'] = 'int'
ttype['GE']['float']['int'] = 'int'
ttype['EQ']['float']['int'] = 'int'
ttype['NEQ']['float']['int'] = 'int'
ttype['>']['float']['float'] = 'int'
ttype['<']['float']['float'] = 'int'
ttype['LE']['float']['float'] = 'int'
ttype['GE']['float']['float'] = 'int'
ttype['EQ']['float']['float'] = 'int'
ttype['NEQ']['float']['float'] = 'int'

ttype['+']['string']['string'] = 'string'

ttype['>']['string']['string'] = 'int'
ttype['<']['string']['string'] = 'int'
ttype['LE']['string']['string'] = 'int'
ttype['GE']['string']['string'] = 'int'
ttype['EQ']['string']['string'] = 'int'
ttype['NEQ']['string']['string'] = 'int'

#    przypisanie liczby całkowitej do zmiennoprzecinkowej,


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
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


class TypeChecker(NodeVisitor):

    def visit_BinExpr(self, node):

        type1 = self.visit(node.left)
        type2 = self.visit(node.right)

    def visit_Const(self, node):


    def visit_Declaration(self, node):

    def visit_ReturnInstr(self, node):
    def visit_PrintInstr(self, node):

    def visit_Init(self, node):
    def visit_AssignmentInstr(self, node):
    def visit_ChoiceInstr(self, node):
    def visit_WhileIstr(self, node):
    def visit_RepeatInstr(self, node):
    def visit_ContinueInstr(self, node):
    def visit_BreakInstr(self, node):
    def visit_CompoundInstr(self, node):
    def visit_CastFunction(self, node):
    def visit_ExprInBrackets(self, node):
    def visit_ExprList(self, node):
    def visit_FunctionList(self, node):
    def visit_Function(self, node):

    def visit_Argument(self, node):
    def visit_Block(self, node):

    def visit_Integer(self, node):
        return 'int'
    def visit_Float(self,node):
        return 'float'
    def visit_String(self,node):
        return 'string'
