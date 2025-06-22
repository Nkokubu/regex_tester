import re

def regex_tester():
    print("🧪 Welcome to the Regex Tester 9000!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        # Get regex pattern from user
        pattern = input("Enter your regex pattern: ")
        if pattern.lower() == "exit":
            print("Goodbye, regex wrangler!")
            break

        # Get test string from user
        test_string = input("Enter the test string: ")
        if test_string.lower() == "exit":
            print("Farewell, text whisperer!")
            break

        try:
            # Compile the pattern to check for syntax errors
            compiled_pattern = re.compile(pattern)
            matches = list(compiled_pattern.finditer(test_string))

            if matches:
                print(f"\n✅ {len(matches)} match(es) found:")
                for match in matches:
                    print(f" - Matched: '{match.group()}' at position {match.start()} to {match.end()}")
            else:
                print("\n❌ No matches found. Try again with a different pattern.")

        except re.error as e:
            print(f"\n🚨 Regex error: {e}. Try fixing your pattern.\n")

        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    regex_tester()
