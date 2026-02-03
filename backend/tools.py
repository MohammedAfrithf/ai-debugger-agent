from langchain.tools import tool

@tool("detect_language")
def detect_language(code: str) -> str:
    """
    Detect the programming language of the given code.
    Return only the language name.
    """
    return f"""
            Identify the programming language of the following code.
            Return only the language name.

            Code:
            {code}
            """



@tool
def detect_errors(code: str, language: str) -> str:
    """
    Identify errors in the given code based on the programming language.
    """
    return f"""
        You are an expert {language} debugger.

        Analyze the {language} code below and list:
        1. Syntax errors
        2. Runtime issues
        3. Logical or best-practice problems

        Code:
        {code}
        """


@tool
def explain_code(code: str, language: str) -> str:
    """
    Explain the given code line by line in simple terms.
    """
    return f"""
        Explain the following {language} code line by line.
        Assume the user is a beginner.

        Code:
        {code}
        """


@tool
def suggest_fix(code: str, language: str) -> str:
    """
    Fix the issues in the given code.
    """
    return f"""
        Fix the issues in the following {language} code.
        Return:
        1. Corrected code
        2. Explanation of what was fixed and why

        Code:
        {code}
        """
