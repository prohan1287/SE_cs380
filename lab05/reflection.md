\# Reflection



> The uploaded three-page handout describes the reflection deliverable but does not include the four reflection-question prompts. These are concise draft reflections on the lab's stated learning outcomes; replace or map them to the exact questions if your instructor provides a separate question sheet.



\### 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps identify likely bugs, insecure coding patterns, and style problems early, making software easier to maintain and review.



\### 2. How do Pylint, Bandit, and Flake8 differ?

Pylint focuses on code quality, potential logical problems, naming, and maintainability. Bandit checks Python code for common security risks. Flake8 checks style and common formatting errors, including many PEP 8 violations. Using all three gives broader coverage than relying on only one tool.



\### 3. What issues were identified and how were they fixed?

The original program used a mutable list as a default argument and constructed an SQL statement using string interpolation. It also used broad exception handlers that could hide database errors. The updated version uses a `None` default with a fresh list, parameterized SQL, and explicit handling of an empty query result. Function names and formatting were also improved.



\### 4. What did you learn about the limitations of static analysis?

Static analysis can flag suspicious code, but it cannot prove that the program behaves correctly in every situation. A developer must review each warning, understand the program's intended behavior, and run functional tests after making changes. The tools complement testing and code review rather than replacing them.

