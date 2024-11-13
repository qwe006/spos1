%{

%}
quotes  \"([^\\\"]|\\.)*\"
comment ("//".*)
comment2 ("/*".*"*/")
%%


public|private|protected { printf("%s : is an Access specifier\n", yytext); }
class|System|out|println|void|main|static { printf("%s : is a Keyword\n", yytext); }
int|double|char|String { printf("%s : is a DataType\n", yytext); }
[A-Z][a-zA-Z0-9]* { printf("%s : is a Class-Name\n", yytext); } 
[a-z][a-zA-Z0-9]* { printf("%s : is a Variable\n", yytext); }  


"+"|"-"|"<"|">"|"!"|"%"|"&"|"^"|"*"|"?"|"=" { printf("%s : is an Operator\n", yytext); }
"["|"]"|"{"|"}"|"("|")"  { printf("%s : is a Bracket\n", yytext); }
","|"."|":"|";" { printf("%s : is a Delimiter\n", yytext); }

[0-9]+ { printf("%s : is a Number\n", yytext); }
{quotes} { printf("%s : is a Quote\n", yytext); }
{comment} { printf("%s : is a Comment\n", yytext); }
{comment2} {printf(" %s : is a Multiline Comment\n",yytext);}
%%


main(int argc, char **argv) {
    if(argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if(!file) {
            fprintf(stderr, "Could not open %s\n", argv[1]);
            exit(1);
        }
        yyin = file; 
    } else {
        yyin = stdin; 
    }
    yylex(); 
    return 0;
}

int yywrap() {
    return 1;
}


#output
C:\Users\SOHAN\OneDrive\Desktop\Sohan>flex lexical.l .......sent 1

C:\Users\SOHAN\OneDrive\Desktop\Sohan>gcc lex.yy.c.........sent 2
lexical.l:28:1: warning: return type defaults to 'int' [-Wimplicit-int]
 main(int argc, char **argv) {
 ^~~~

C:\Users\SOHAN\OneDrive\Desktop\Sohan>a.exe  ..............sent 3
10
10 : is a Number

public class Hello {publicstatic:void main(string args[]){int i=0;system.out.println("Hello Everyone");}}
public : is an Access specifier
 class : is a Keyword
 Hello : is a Class-Name
 { : is a Bracket
publicstatic : is a Variable
: : is a Delimiter
void : is a Keyword
 main : is a Keyword
( : is a Bracket
string : is a Variable
 args : is a Variable
[ : is a Bracket
] : is a Bracket
) : is a Bracket
{ : is a Bracket
int : is a DataType
 i : is a Variable
= : is an Operator
0 : is a Number
; : is a Delimiter
system : is a Variable
. : is a Delimiter
out : is a Keyword
. : is a Delimiter
println : is a Keyword
( : is a Bracket
"Hello Everyone" : is a Quote
) : is a Bracket
; : is a Delimiter
} : is a Bracket
} : is a Bracket