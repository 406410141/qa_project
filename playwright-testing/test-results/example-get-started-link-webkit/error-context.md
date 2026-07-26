# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: example.spec.ts >> get started link
- Location: test/example.spec.ts:10:5

# Error details

```
Error: browserType.launch: Target page, context or browser has been closed
Browser logs:

<launching> /Users/tung/Library/Caches/ms-playwright/webkit_mac14_arm64_special-2251/pw_run.sh --inspector-pipe --headless --no-startup-window
<launched> pid=16119
[pid=16119][err] /Users/tung/Library/Caches/ms-playwright/webkit_mac14_arm64_special-2251/pw_run.sh: line 7: 16125 Bus error: 10           DYLD_FRAMEWORK_PATH="$DYLIB_PATH" DYLD_LIBRARY_PATH="$DYLIB_PATH" "$PLAYWRIGHT" "$@"
Call log:
  - <launching> /Users/tung/Library/Caches/ms-playwright/webkit_mac14_arm64_special-2251/pw_run.sh --inspector-pipe --headless --no-startup-window
  - <launched> pid=16119
  - [pid=16119][err] /Users/tung/Library/Caches/ms-playwright/webkit_mac14_arm64_special-2251/pw_run.sh: line 7: 16125 Bus error: 10           DYLD_FRAMEWORK_PATH="$DYLIB_PATH" DYLD_LIBRARY_PATH="$DYLIB_PATH" "$PLAYWRIGHT" "$@"
  - [pid=16119] <gracefully close start>
  - [pid=16119] <kill>
  - [pid=16119] <will force kill>
  - [pid=16119] exception while trying to kill process: Error: kill ESRCH
  - [pid=16119] <process did exit: exitCode=138, signal=null>
  - [pid=16119] starting temporary directories cleanup
  - [pid=16119] finished temporary directories cleanup
  - [pid=16119] <gracefully close end>

```