# loader.dll

## Imports

<details><summary><b>d3d9.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 9 | Direct3DCreate9 |

</p></details>
<details><summary><b>KERNEL32.dll</b> (173)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 627 | GetModuleFileNameA |
| 632 | GetModuleHandleW |
| 963 | LoadLibraryExW |
| 964 | LoadLibraryW |
| 1294 | SetDllDirectoryW |
| 173 | CopyFileW |
| 1003 | MoveFileW |
| 470 | GetCommandLineA |
| 471 | GetCommandLineW |
| 134 | CloseHandle |
| 609 | GetLastError |
| 1301 | SetErrorMode |
| 1495 | WaitForSingleObject |
| 572 | GetExitCodeProcess |
| 1229 | ResumeThread |
| 427 | FreeLibrary |
| 686 | GetProcAddress |
| 962 | LoadLibraryExA |
| 961 | LoadLibraryA |
| 919 | K32EnumProcessModules |
| 931 | K32GetModuleFileNameExW |
| 936 | K32GetProcessMemoryInfo |
| 1473 | VerSetConditionMask |
| 529 | GetCurrentDirectoryW |
| 373 | FindClose |
| 384 | FindFirstFileW |
| 396 | FindNextFileW |
| 576 | GetFileAttributesA |
| 601 | GetFullPathNameW |
| 622 | GetLongPathNameW |
| 717 | GetShortPathNameW |
| 1139 | ReadFile |
| 758 | GetTempPathW |
| 1330 | SetLastError |
| 1101 | QueryPerformanceCounter |
| 1102 | QueryPerformanceFrequency |
| 862 | InitializeCriticalSection |
| 305 | EnterCriticalSection |
| 957 | LeaveCriticalSection |
| 272 | DeleteCriticalSection |
| 539 | GetCurrentThread |
| 540 | GetCurrentThreadId |
| 773 | GetThreadTimes |
| 1037 | OpenProcess |
| 743 | GetSystemTime |
| 610 | GetLocalTime |
| 628 | GetModuleFileNameW |
| 813 | GlobalAlloc |
| 831 | GlobalUnlock |
| 824 | GlobalLock |
| 552 | GetDiskFreeSpaceExW |
| 423 | FormatMessageW |
| 1477 | VerifyVersionInfoW |
| 1309 | SetFileAttributesW |
| 252 | CreateToolhelp32Snapshot |
| 1068 | Process32FirstW |
| 1070 | Process32NextW |
| 551 | GetDiskFreeSpaceExA |
| 615 | GetLogicalDriveStringsW |
| 1093 | QueryDosDeviceW |
| 215 | CreateMutexA |
| 573 | GetExitCodeThread |
| 745 | GetSystemTimeAsFileTime |
| 794 | GetVersionExA |
| 362 | FileTimeToSystemTime |
| 921 | K32EnumProcesses |
| 935 | K32GetProcessImageFileNameW |
| 1067 | Process32First |
| 1069 | Process32Next |
| 229 | CreateProcessW |
| 970 | LocalAlloc |
| 224 | CreateProcessA |
| 736 | GetSystemDirectoryW |
| 1584 | lstrcmpW |
| 354 | ExpandEnvironmentStringsW |
| 1583 | lstrcmpA |
| 1049 | OutputDebugStringW |
| 277 | DeleteFileW |
| 203 | CreateFileW |
| 186 | CreateDirectoryW |
| 1289 | SetCurrentDirectoryW |
| 1293 | SetDllDirectoryA |
| 1405 | Sleep |
| 629 | GetModuleHandleA |
| 1553 | WriteConsoleW |
| 846 | HeapSize |
| 692 | GetProcessHeap |
| 426 | FreeEnvironmentStringsW |
| 567 | GetEnvironmentStringsW |
| 663 | GetOEMCP |
| 434 | GetACP |
| 907 | IsValidCodePage |
| 379 | FindFirstFileExW |
| 1354 | SetStdHandle |
| 844 | HeapReAlloc |
| 1136 | ReadConsoleW |
| 1315 | SetFilePointerEx |
| 588 | GetFileSizeEx |
| 490 | GetConsoleCP |
| 340 | EnumSystemLocalesW |
| 786 | GetUserDefaultLCID |
| 909 | IsValidLocale |
| 1209 | RemoveDirectoryW |
| 581 | GetFileAttributesW |
| 998 | MoveFileA |
| 913 | IsWow64Process |
| 1420 | TerminateProcess |
| 350 | ExitProcess |
| 536 | GetCurrentProcessId |
| 535 | GetCurrentProcess |
| 1206 | RemoveDirectoryA |
| 1288 | SetCurrentDirectoryA |
| 1000 | MoveFileExW |
| 1306 | SetFileAttributesA |
| 975 | LocalFree |
| 1486 | VirtualQuery |
| 416 | FlushInstructionCache |
| 1484 | VirtualProtect |
| 867 | InitializeSListHead |
| 720 | GetStartupInfoW |
| 895 | IsDebuggerPresent |
| 902 | IsProcessorFeaturePresent |
| 837 | HeapAlloc |
| 841 | HeapFree |
| 631 | GetModuleHandleExW |
| 1389 | SetUnhandledExceptionFilter |
| 1453 | UnhandledExceptionFilter |
| 727 | GetStringTypeW |
| 613 | GetLocaleInfoW |
| 945 | LCMapStringW |
| 1439 | TlsFree |
| 1235 | RtlUnwind |
| 1122 | RaiseException |
| 876 | InterlockedFlushSList |
| 1441 | TlsSetValue |
| 1440 | TlsGetValue |
| 35 | AreFileApisANSI |
| 155 | CompareStringW |
| 1007 | MultiByteToWideChar |
| 1534 | WideCharToMultiByte |
| 449 | GetCPInfo |
| 893 | IsDBCSLeadByte |
| 361 | FileTimeToLocalFileTime |
| 972 | LocalFileTimeToFileTime |
| 1417 | SystemTimeToTzSpecificLocalTime |
| 1449 | TzSpecificLocalTimeToSystemTime |
| 1416 | SystemTimeToFileTime |
| 420 | FoldStringW |
| 191 | CreateEventW |
| 1374 | SetThreadPriority |
| 1367 | SetThreadExecutionState |
| 795 | GetVersionExW |
| 1302 | SetEvent |
| 1222 | ResetEvent |
| 1204 | ReleaseSemaphore |
| 236 | CreateSemaphoreW |
| 243 | CreateThread |
| 687 | GetProcessAffinityMask |
| 1318 | SetFileTime |
| 285 | DeviceIoControl |
| 722 | GetStdHandle |
| 415 | FlushFileBuffers |
| 590 | GetFileType |
| 1296 | SetEndOfFile |
| 1314 | SetFilePointer |
| 1554 | WriteFile |
| 508 | GetConsoleMode |
| 207 | CreateHardLinkW |
| 1496 | WaitForSingleObjectEx |
| 301 | EncodePointer |
| 265 | DecodePointer |
| 863 | InitializeCriticalSectionAndSpinCount |
| 1438 | TlsAlloc |

</p></details>
<details><summary><b>USER32.dll</b> (35)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 105 | CreateDialogParamA |
| 106 | CreateDialogParamW |
| 58 | CharToOemBuffW |
| 879 | SetWindowPos |
| 896 | ShowWindow |
| 181 | DestroyWindow |
| 387 | GetMessageA |
| 928 | TranslateMessage |
| 188 | DispatchMessageA |
| 676 | PeekMessageA |
| 780 | SendMessageA |
| 884 | SetWindowTextW |
| 482 | GetWindowInfo |
| 263 | EnumThreadWindows |
| 646 | MessageBoxW |
| 232 | EmptyClipboard |
| 795 | SetClipboardData |
| 79 | CloseClipboard |
| 663 | OpenClipboard |
| 273 | FindWindowA |
| 491 | GetWindowRect |
| 495 | GetWindowTextA |
| 815 | SetForegroundWindow |
| 452 | GetSystemMetrics |
| 775 | SendDlgItemMessageA |
| 556 | IsDlgButtonChecked |
| 71 | CheckRadioButton |
| 66 | CheckDlgButton |
| 330 | GetDlgItem |
| 56 | CharToOemA |
| 658 | OemToCharA |
| 659 | OemToCharBuffA |
| 63 | CharUpperW |
| 49 | CharLowerW |
| 680 | PostMessageA |

</p></details>
<details><summary><b>GDI32.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 5 | AddFontResourceExW |
| 798 | RemoveFontResourceExW |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (15)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 627 | RegDeleteValueW |
| 308 | FreeSid |
| 95 | CheckTokenMembership |
| 32 | AllocateAndInitializeSid |
| 681 | RegSetValueExW |
| 665 | RegQueryValueExW |
| 652 | RegOpenKeyExW |
| 638 | RegFlushKey |
| 616 | RegDeleteKeyA |
| 612 | RegCreateKeyExW |
| 603 | RegCloseKey |
| 533 | OpenProcessToken |
| 31 | AdjustTokenPrivileges |
| 431 | LookupPrivilegeValueW |
| 732 | SetFileSecurityW |

</p></details>
<details><summary><b>SHELL32.dll</b> (13)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 7 | CommandLineToArgvW |
| 344 | SHGetFolderPathW |
| 340 | SHGetFolderPathA |
| 439 | ShellExecuteW |
| 392 | SHOpenFolderAndSelectItems |
| 190 |  |
| 155 |  |
| 321 | SHFileOperationW |
| 438 | ShellExecuteExW |
| 356 | SHGetMalloc |
| 364 | SHGetPathFromIDListW |
| 135 | SHBrowseForFolderW |
| 435 | ShellExecuteA |

</p></details>
<details><summary><b>ole32.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 40 | CoCreateInstance |
| 132 | CoSetProxyBlanket |
| 95 | CoInitializeSecurity |
| 94 | CoInitializeEx |

</p></details>
<details><summary><b>OLEAUT32.dll</b> (6)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 12 |  |
| 9 |  |
| 7 |  |
| 6 |  |
| 2 |  |
| 150 |  |

</p></details>
<details><summary><b>SHLWAPI.dll</b> (2)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 89 | PathGetDriveNumberW |
| 57 | PathBuildRootW |

</p></details>
<details><summary><b>WINMM.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 148 | timeGetTime |

</p></details>
<details><summary><b>VERSION.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 15 | VerQueryValueA |
| 8 | GetFileVersionInfoW |
| 7 | GetFileVersionInfoSizeW |

</p></details>
<details><summary><b>WINTRUST.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 143 | WinVerifyTrust |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | DoWinMain |
| 2 | GetLibMtaVersion |

</p></details>
