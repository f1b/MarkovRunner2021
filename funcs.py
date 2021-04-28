import re

template = r"""(?mx)
^(?: 
  (?: (?P<rule>    (?P<inp> .+? ) \s+ -> \s+ (?P<breakpnt> \.)? (?P<outp> .+) ) )
)$
"""

def GetRules(rules_in):
    return [(matchobj.group('inp'), matchobj.group('outp'), bool(matchobj.group('breakpnt'))) for matchobj in re.finditer(template, rules_in) if matchobj.group('rule')]
 
def MarkovReplace(word, rules):
    while True:
        for inp, outp, breakpnt in rules:
            if inp in word:
                word = word.replace(inp, outp, 1)
                word = word.replace("E","")
                print(word)
                if breakpnt:
                    return word
                break
        else:
            return word