# MTA Server64.exe

## Imports

<details><summary><b>KERNEL32.dll</b> (87)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 420 | FreeLibrary |
| 676 | GetProcAddress |
| 936 | LoadLibraryA |
| 1446 | VerSetConditionMask |
| 1266 | SetCurrentDirectoryW |
| 366 | FindClose |
| 127 | CloseHandle |
| 1072 | QueryPerformanceCounter |
| 848 | InitializeCriticalSection |
| 297 | EnterCriticalSection |
| 933 | LeaveCriticalSection |
| 262 | DeleteCriticalSection |
| 528 | GetCurrentProcessId |
| 532 | GetCurrentThreadId |
| 617 | GetModuleFileNameW |
| 1450 | VerifyVersionInfoW |
| 833 | HeapSize |
| 1520 | WriteConsoleW |
| 194 | CreateFileW |
| 408 | FlushFileBuffers |
| 1279 | SetEvent |
| 1190 | ResetEvent |
| 1468 | WaitForSingleObjectEx |
| 182 | CreateEventW |
| 621 | GetModuleHandleW |
| 733 | GetSystemTimeAsFileTime |
| 852 | InitializeSListHead |
| 1198 | RtlCaptureContext |
| 1205 | RtlLookupFunctionEntry |
| 1212 | RtlVirtualUnwind |
| 874 | IsDebuggerPresent |
| 1426 | UnhandledExceptionFilter |
| 1362 | SetUnhandledExceptionFilter |
| 709 | GetStartupInfoW |
| 880 | IsProcessorFeaturePresent |
| 527 | GetCurrentProcess |
| 1392 | TerminateProcess |
| 1501 | WideCharToMultiByte |
| 980 | MultiByteToWideChar |
| 293 | EncodePointer |
| 255 | DecodePointer |
| 1305 | SetLastError |
| 849 | InitializeCriticalSectionAndSpinCount |
| 1410 | TlsAlloc |
| 1412 | TlsGetValue |
| 1413 | TlsSetValue |
| 1411 | TlsFree |
| 147 | CompareStringW |
| 921 | LCMapStringW |
| 602 | GetLocaleInfoW |
| 716 | GetStringTypeW |
| 441 | GetCPInfo |
| 1207 | RtlPcToFileHeader |
| 1092 | RaiseException |
| 1211 | RtlUnwindEx |
| 598 | GetLastError |
| 938 | LoadLibraryExW |
| 1108 | ReadFile |
| 711 | GetStdHandle |
| 1521 | WriteFile |
| 616 | GetModuleFileNameA |
| 343 | ExitProcess |
| 620 | GetModuleHandleExW |
| 462 | GetCommandLineA |
| 463 | GetCommandLineW |
| 426 | GetACP |
| 824 | HeapAlloc |
| 828 | HeapFree |
| 831 | HeapReAlloc |
| 887 | IsValidLocale |
| 773 | GetUserDefaultLCID |
| 332 | EnumSystemLocalesW |
| 581 | GetFileType |
| 500 | GetConsoleMode |
| 1106 | ReadConsoleW |
| 1292 | SetFilePointerEx |
| 482 | GetConsoleCP |
| 371 | FindFirstFileExA |
| 387 | FindNextFileA |
| 885 | IsValidCodePage |
| 653 | GetOEMCP |
| 558 | GetEnvironmentStringsW |
| 419 | FreeEnvironmentStringsW |
| 1276 | SetEnvironmentVariableA |
| 1328 | SetStdHandle |
| 681 | GetProcessHeap |
| 1273 | SetEndOfFile |

</p></details>
<details><summary><b>SHLWAPI.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 143 | PathRemoveFileSpecW |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 138 | timeGetTime |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | GetLibMtaVersion |

</p></details>
