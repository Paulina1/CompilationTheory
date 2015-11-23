from collections import defaultdict
import AST
from SymbolTab import SymbolTable, FunctionSymbol, VariableSymbol
import re


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

#    przypisanie liczby calkowitej do zmiennoprzecinkowej,


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
            if node is not None:
                for child in node.children():
                    if isinstance(child, list):
                        for item in child:
                            if isinstance(item, AST.Node):
                                self.visit(item)
                    elif isinstance(child, AST.Node):
                        self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.scope = SymbolTable(None, 'main')

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        print type1
        print type2
        print node.op
        if ttype[node.op][type1][type2] is None:
            print "Bad expression {} in line {}".format(node.op, '')
        return ttype[node.op][type1][type2]

    def visit_Const(self, node):
        if re.match(r"(\+|-){0,1}(\d+\.\d+|\.\d+)", node.val):
            return self.visit_Float(node)
        elif re.match(r"(\+|-){0,1}\d+", node.val):
            return self.visit_Integer(node)
        else:
            return self.visit_String(node)


    def visit_Integer(self, node):
        return 'int'

    def visit_Float(self,node):
        return 'float'

    def visit_String(self,node):
        return 'string'

    def visit_Declaration(self, node):
        visited_inits = self.visit(node.inits)
        if visited_inits is not None:
            for curr in self.visit(node.inits):
                if self.scope.get(curr[0]) is not None:
                    print "Variable {} in line {} has been declared earlier".format(curr[0], '')
                else:
                    if node.type == curr[1]:
                        self.scope.put(curr[0], VariableSymbol(curr[0], node.type))
                    else:
                        print "Type mismatch in line {}".format('')

    def visit_ReturnInstr(self, node):
        if self.scope.parent.get(self.scope.name).type != self.visit(node.expr):
            print "Type mismatch in line {}".format('')

    def visit_PrintInstr(self, node):
        self.visit(node.expr)

    def visit_Init(self, node):
        return (node.id, self.visit(node.expr))

    def visit_AssignmentInstr(self, node):
        return (node.id, self.visit(node.expr))

    def visit_ChoiceInstr(self, node):
        self.visit(node.condition)
        self.visit(node.instruction)
        self.visit(node.else_instr)

    def visit_WhileInstr(self, node):
        self.visit(node.condition)
        self.scope = self.scope.pushScope("loop")
        self.visit(node.instruction)
        self.scope = self.scope.popScope()

    def visit_RepeatInstr(self, node):
        self.visit(node.condition)
        self.scope = self.scope.pushScope("loop")
        self.visit(node.instruction)
        self.scope = self.scope.popScope()

    def visit_ContinueInstr(self, node):
        if self.scope.name != "loop":
            print "Continue outside the loop in line {}".format('')

    def visit_BreakInstr(self, node):
        if self.scope.name != "loop":
            print "Break outside the loop in line {}".format('')

    def visit_CompoundInstr(self, node):
        self.visit(node.declarations)
        self.visit(node.instructions_opt)

    def visit_CastFunction(self, node):
        if self.scope.get(node.functionName) is None:
            print "Function {} in line {} has not been declared".format(node.functionName, '')
        else:
            args = self.scope.get(node.functionName).arguments
            if self.visit(args) != self.visit(node.args):
                print "Argument mismatch in line {}".format('')


    def visit_ExprInBrackets(self, node):
        return self.visit(node.expr)

    def visit_Function(self, node):
        if self.scope.get(node.id) is not None:
            print "Function {} in line {} has been declared earlier".format(node.id, '')
        else:
            self.visit(node.args_list_or_empty)
            self.scope.put(node.id, FunctionSymbol(node.id, node.type, node.args_list_or_empty))
            self.scope = self.scope.pushScope(node.id)
            self.visit(node.compound_instr)
            self.scope = self.scope.popScope()

    def visit_Argument(self, node):
        return (node.type, node.id)

    def visit_Block(self, node):
        self.scope = self.scope.pushScope("block")
        self.visit(node.declarations)
        self.visit(node.fundefs_opt)
        self.visit(node.instructions_opt)
        self.scope = self.scope.popScope()
