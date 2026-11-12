\# Static Analysis Issue Log



> Initial issue candidates are based on direct inspection of the assigned `pet\_shelter.py`. Run the tools locally and update the line numbers/codes to match the actual reports before submission.



| Issue | Type | Line(s) in original file | Description | Fix Approach |

|---|---|---:|---|---|

| SQL query built with string interpolation | Security | 11 | Pet name/species are inserted directly into SQL, allowing SQL injection and breaking on quotes. | Use SQLite parameter placeholders (`?`) and pass values separately. |

| Mutable default argument (`tags=\[]`) | Bug | 9 | The same list is reused across calls, so tags can leak between registrations. | Use `None` as the default and create/copy a list inside the function. |

| Bare `except:` | Reliability | 30–32 | Suppresses every exception, including errors unrelated to an empty result. | Remove the broad handler and explicitly check whether `fetchone()` returned a row. |

| Broad exception swallowed with `pass` | Reliability | 40–42 | Database failures are silently ignored, making failures difficult to diagnose. | Remove the blanket handler; let unexpected database errors surface or handle a specific expected exception. |

| Missing `LIMIT 1` in oldest-pet query | Efficiency | 28 | The query fetches all matching rows even though only the oldest row is needed. | Add `LIMIT 1`. |

| Non-PEP 8 function names | Style | 9, 17, 24, 26, 34 | CamelCase function names violate the usual Python naming convention. | Rename functions to `snake\_case`. |

| One-line conditional | Style | 36 | Conditional and return share one line, reducing readability. | Use a normal multi-line `if` or conditional expression. |

| Module executes demo on import | Maintainability | 47 | Calling `main()` unconditionally runs the demo whenever the module is imported. | Guard execution with `if \_\_name\_\_ == "\_\_main\_\_":`. |



\## Tool verification



The execution environment used to prepare this folder did not have Pylint, Bandit, or Flake8 installed and could not reach the package index. Therefore, no tool findings or scores are fabricated here. Run the commands in `RUN\_ME.md` on your machine and update this table with the exact reported codes/line numbers.

