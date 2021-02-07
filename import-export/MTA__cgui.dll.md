# cgui.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (101)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 373 | FindClose |
| 396 | FindNextFileW |
| 576 | GetFileAttributesA |
| 601 | GetFullPathNameW |
| 622 | GetLongPathNameW |
| 1139 | ReadFile |
| 1306 | SetFileAttributesA |
| 134 | CloseHandle |
| 609 | GetLastError |
| 1101 | QueryPerformanceCounter |
| 1102 | QueryPerformanceFrequency |
| 862 | InitializeCriticalSection |
| 305 | EnterCriticalSection |
| 957 | LeaveCriticalSection |
| 272 | DeleteCriticalSection |
| 1495 | WaitForSingleObject |
| 536 | GetCurrentProcessId |
| 539 | GetCurrentThread |
| 540 | GetCurrentThreadId |
| 773 | GetThreadTimes |
| 203 | CreateFileW |
| 743 | GetSystemTime |
| 610 | GetLocalTime |
| 628 | GetModuleFileNameW |
| 686 | GetProcAddress |
| 252 | CreateToolhelp32Snapshot |
| 1068 | Process32FirstW |
| 1070 | Process32NextW |
| 931 | K32GetModuleFileNameExW |
| 1296 | SetEndOfFile |
| 846 | HeapSize |
| 1354 | SetStdHandle |
| 692 | GetProcessHeap |
| 426 | FreeEnvironmentStringsW |
| 567 | GetEnvironmentStringsW |
| 471 | GetCommandLineW |
| 470 | GetCommandLineA |
| 663 | GetOEMCP |
| 824 | GlobalLock |
| 831 | GlobalUnlock |
| 813 | GlobalAlloc |
| 1420 | TerminateProcess |
| 1037 | OpenProcess |
| 535 | GetCurrentProcess |
| 434 | GetACP |
| 907 | IsValidCodePage |
| 379 | FindFirstFileExW |
| 415 | FlushFileBuffers |
| 782 | GetTimeZoneInformation |
| 588 | GetFileSizeEx |
| 490 | GetConsoleCP |
| 1315 | SetFilePointerEx |
| 1136 | ReadConsoleW |
| 508 | GetConsoleMode |
| 340 | EnumSystemLocalesW |
| 786 | GetUserDefaultLCID |
| 909 | IsValidLocale |
| 1496 | WaitForSingleObjectEx |
| 1534 | WideCharToMultiByte |
| 301 | EncodePointer |
| 265 | DecodePointer |
| 1007 | MultiByteToWideChar |
| 1330 | SetLastError |
| 863 | InitializeCriticalSectionAndSpinCount |
| 191 | CreateEventW |
| 1438 | TlsAlloc |
| 1440 | TlsGetValue |
| 1441 | TlsSetValue |
| 1439 | TlsFree |
| 745 | GetSystemTimeAsFileTime |
| 632 | GetModuleHandleW |
| 155 | CompareStringW |
| 945 | LCMapStringW |
| 613 | GetLocaleInfoW |
| 727 | GetStringTypeW |
| 449 | GetCPInfo |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 902 | IsProcessorFeaturePresent |
| 1453 | UnhandledExceptionFilter |
| 1389 | SetUnhandledExceptionFilter |
| 895 | IsDebuggerPresent |
| 720 | GetStartupInfoW |
| 867 | InitializeSListHead |
| 1049 | OutputDebugStringW |
| 427 | FreeLibrary |
| 963 | LoadLibraryExW |
| 876 | InterlockedFlushSList |
| 1122 | RaiseException |
| 1235 | RtlUnwind |
| 722 | GetStdHandle |
| 590 | GetFileType |
| 631 | GetModuleHandleExW |
| 1553 | WriteConsoleW |
| 350 | ExitProcess |
| 1300 | SetEnvironmentVariableW |
| 186 | CreateDirectoryW |
| 1554 | WriteFile |
| 841 | HeapFree |
| 837 | HeapAlloc |
| 844 | HeapReAlloc |

</p></details>
<details><summary><b>USER32.dll</b> (7)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 663 | OpenClipboard |
| 79 | CloseClipboard |
| 795 | SetClipboardData |
| 308 | GetClipboardData |
| 646 | MessageBoxW |
| 639 | MessageBoxA |
| 232 | EmptyClipboard |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (6)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 665 | RegQueryValueExW |
| 652 | RegOpenKeyExW |
| 638 | RegFlushKey |
| 612 | RegCreateKeyExW |
| 603 | RegCloseKey |
| 681 | RegSetValueExW |

</p></details>
<details><summary><b>SHELL32.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 435 | ShellExecuteA |
| 438 | ShellExecuteExW |
| 344 | SHGetFolderPathW |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 148 | timeGetTime |

</p></details>
<details><summary><b>d3dx9_42.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 97 | D3DXCreateTextureFromFileInMemoryEx |
| 92 | D3DXCreateTexture |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | GetLibMtaVersion |
| 2 | InitGUIInterface |

</p></details>
