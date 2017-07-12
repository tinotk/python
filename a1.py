'''
Syntax vs Semantics
Generates a random syntactically correct C++ program using pre-defined set of productions rules.
Consider the following set of productions that define a subset of the C++ programming
language:
<prog> ::= “int main() { <stat_list> return 0; }”
<stat_list> ::= <stat>
			| <stat_list> <stat>
<stat> 	::= <cmpd_stat>
		| <if_stat>
		| <iter_stat>
		| <assgn_stat>
		| <decl_stat>
<cmpd_stat> ::= { <stat_list> }
<if_stat> 	::= if ( <exp> ) <stat>
			| if ( <exp> ) <cmpd_stat>
			| if ( <exp> ) <stat> else <stat>
			| if ( <exp> ) <cmpd_stat> else <stat>
			| if ( <exp> ) <stat> else <cmpd_stat>
			| if ( <exp> ) <cmpd_stat> else <cmpd_stat>
<iter_stat> ::= while ( <exp> ) <stat>
			| while ( <exp> ) <cmpd_stat>
<assgn_stat> ::= <id> = <exp> ;
<decl_stat> ::= <type> <id> ;
			| <type> <assgn_stat>
<exp> 	::= <exp> <op> <exp>
		| <id>
		| <const>
<op> 	::= + | - | * | /
<type> 	::= int
		| double
<id> 	::= <char><chardigit_seq>
<const> ::= <digit><digit_seq>
<char_digit_seq> 	::= [empty]
					| <char><char_digit_seq>
					| <digit><char_digit_seq>
<digit_seq> ::= [empty]
			| <digit><digit_seq>
<char> ::= [A-Z] | [a-z] | _
<digit> ::= [0-9]

by tinotk
'''

import random
import string

prog = {}
prog["prog"] = ["int main() {\n<stat_list>\nreturn 0;\n}"]
prog["stat_list"] = ["<stat>","<stat_list> <stat>"]
prog["stat"] = ["<cmpd_stat>","<if_stat>","<iter_stat>","<assgn_stat>","<decl_stat>"]
prog["cmpd_stat"] = ["{\n\t<stat_list>\n}"]
prog["if_stat"] = ["if ( <exp> )\n<stat>", "if ( <exp> )\n<cmpd_stat>", "if ( <exp> )\n<stat> else\n<stat>", "if ( <exp> )\n<cmpd_stat>\nelse\n<stat>", "if ( <exp> )\n<stat>\nelse \n<cmpd_stat>", "if ( <exp> ) \n<cmpd_stat>\nelse <cmpd_stat>"]
prog["iter_stat"] = ["while ( <exp> ) {\n<stat>\n}", "while ( <exp> ) {\n\t<cmpd_stat>\n}"]
prog["assgn_stat"] = ["<id> = <exp>;"]
prog["decl_stat"] = ["<type> <id>;", "<type> <assgn_stat>"]
prog["exp"] = ["<exp> <op> <exp>", "<id>", "<const>"]
prog["op"] = ["+", "-", "*", "/"]
prog["type"] = ["int", "double"]
prog["id"] = ["<char><char_digit_seq>"]
prog["const"] = ["<digit><digit_seq>"]
prog["char_digit_seq"] = ["", "<char><char_digit_seq>", "<digit><char_digit_seq>"]
prog["digit_seq"] = ["", "<digit><digit_seq>"]
prog["char"] = list(string.ascii_letters+"_")
prog["digit"] = list(string.digits)

temp = "<prog>"

if __name__ == "__main__":
    while temp.find("<") != -1:
        start = temp.find("<")
        end = temp.find(">")
        # print(random.choice(list(prog[temp[start+1:end]]))) #print random list item from extracted key
        # print(random.choice(prog[random.choice(list(prog.keys()))])) #print random value from randomly selected key from list

        a = random.choice(list(prog[temp[start + 1:end]]))
        temp = temp.replace(temp[start:end + 1], str(a), 1)
        if (len(temp) > 1000):
            break
    print(temp)
