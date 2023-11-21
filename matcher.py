import re

# Pattern to determine if a given line contains a C++ method declaration
method_pattern = re.compile(
    r'\b(public|private|protected|internal)?\s*(?:static\s+)?\w+\s+\w+\s*\([^)]*\)\s*(?:{[^}]*})?'
)

# Test cases to determine if the regex is functioning correctly
test_cases = [
    "static void poop()", "bool myFunction()", "int myFunc(int poop)",
    "public void hello()", "public static void hello()", "hello", "goodbye()",
    "goodbye goodbye()", "double cat(int myCat);", "static void poop(){}",
    "bool myFunction(){}", "int myFunc(int poop){}",
    "int myFunc(int test, int test, bool test)"
    "void myFoo(bar)", "Okay okay"
]

for test_case in test_cases:
  if method_pattern.search(test_case):
    print(f"Match: {test_case}")
  else:
    print(f"No match: {test_case}")
