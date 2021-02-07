# xinput1_3_mta.dll

## Imports

<details><summary><b>ntdll.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 918 | RtlUnwind |

</p></details>
<details><summary><b>KERNEL32.dll</b> (77)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 600 | LocalAlloc |
| 790 | SetEvent |
| 369 | GetLastError |
| 111 | CreateThread |
| 86 | CreateFileW |
| 597 | LoadLibraryW |
| 248 | FreeLibrary |
| 416 | GetProcAddress |
| 138 | DeviceIoControl |
| 404 | GetOverlappedResult |
| 80 | CreateEventW |
| 479 | GetTickCount |
| 675 | QueryPerformanceCounter |
| 326 | GetCurrentThreadId |
| 323 | GetCurrentProcessId |
| 458 | GetSystemTimeAsFileTime |
| 862 | TerminateProcess |
| 878 | UnhandledExceptionFilter |
| 842 | SetUnhandledExceptionFilter |
| 272 | GetCommandLineA |
| 534 | HeapFree |
| 489 | GetVersionExA |
| 528 | HeapAlloc |
| 419 | GetProcessHeap |
| 185 | ExitProcess |
| 383 | GetModuleHandleA |
| 867 | TlsAlloc |
| 808 | SetLastError |
| 868 | TlsFree |
| 870 | TlsSetValue |
| 869 | TlsGetValue |
| 854 | Sleep |
| 804 | SetHandleCount |
| 441 | GetStdHandle |
| 358 | GetFileType |
| 439 | GetStartupInfoA |
| 381 | GetModuleFileNameA |
| 246 | FreeEnvironmentStringsA |
| 341 | GetEnvironmentStrings |
| 322 | GetCurrentProcess |
| 916 | WideCharToMultiByte |
| 343 | GetEnvironmentStringsW |
| 532 | HeapDestroy |
| 147 | DuplicateHandle |
| 899 | VirtualFree |
| 932 | WriteFile |
| 553 | InterlockedExchange |
| 904 | VirtualQuery |
| 253 | GetACP |
| 403 | GetOEMCP |
| 260 | GetCPInfo |
| 897 | VirtualAlloc |
| 538 | HeapReAlloc |
| 566 | IsBadWritePtr |
| 594 | LoadLibraryA |
| 679 | RaiseException |
| 563 | IsBadReadPtr |
| 560 | IsBadCodePtr |
| 795 | SetFilePointer |
| 629 | MultiByteToWideChar |
| 372 | GetLocaleInfoA |
| 442 | GetStringTypeA |
| 445 | GetStringTypeW |
| 580 | LCMapStringA |
| 581 | LCMapStringW |
| 823 | SetStdHandle |
| 902 | VirtualProtect |
| 453 | GetSystemInfo |
| 238 | FlushFileBuffers |
| 604 | LocalFree |
| 593 | LeaveCriticalSection |
| 152 | EnterCriticalSection |
| 129 | DeleteCriticalSection |
| 547 | InitializeCriticalSection |
| 52 | CloseHandle |
| 247 | FreeEnvironmentStringsW |
| 530 | HeapCreate |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 633 | TraceMessage |

</p></details>
<details><summary><b>SETUPAPI.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 285 | SetupDiDestroyDeviceInfoList |
| 308 | SetupDiGetClassDevsW |
| 289 | SetupDiEnumDeviceInterfaces |
| 328 | SetupDiGetDeviceInterfaceDetailW |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | DllMain |
| 2 | XInputGetState |
| 3 | XInputSetState |
| 4 | XInputGetCapabilities |
| 5 | XInputEnable |
| 6 | XInputGetDSoundAudioDeviceGuids |
| 7 | XInputGetBatteryInformation |
| 8 | XInputGetKeystroke |
| 9 |  |
| 10 |  |
| 11 |  |
| 12 |  |
| 13 |  |
| 14 |  |
| 15 |  |
| 16 |  |
| 17 |  |
| 18 |  |
| 19 |  |
| 20 |  |
| 21 |  |
| 22 |  |
| 23 |  |
| 24 |  |
| 25 |  |
| 26 |  |
| 27 |  |
| 28 |  |
| 29 |  |
| 30 |  |
| 31 |  |
| 32 |  |
| 33 |  |
| 34 |  |
| 35 |  |
| 36 |  |
| 37 |  |
| 38 |  |
| 39 |  |
| 40 |  |
| 41 |  |
| 42 |  |
| 43 |  |
| 44 |  |
| 45 |  |
| 46 |  |
| 47 |  |
| 48 |  |
| 49 |  |
| 50 |  |
| 51 |  |
| 52 |  |
| 53 |  |
| 54 |  |
| 55 |  |
| 56 |  |
| 57 |  |
| 58 |  |
| 59 |  |
| 60 |  |
| 61 |  |
| 62 |  |
| 63 |  |
| 64 |  |
| 65 |  |
| 66 |  |
| 67 |  |
| 68 |  |
| 69 |  |
| 70 |  |
| 71 |  |
| 72 |  |
| 73 |  |
| 74 |  |
| 75 |  |
| 76 |  |
| 77 |  |
| 78 |  |
| 79 |  |
| 80 |  |
| 81 |  |
| 82 |  |
| 83 |  |
| 84 |  |
| 85 |  |
| 86 |  |
| 87 |  |
| 88 |  |
| 89 |  |
| 90 |  |
| 91 |  |
| 92 |  |
| 93 |  |
| 94 |  |
| 95 |  |
| 96 |  |
| 97 |  |
| 98 |  |
| 99 |  |
| 100 |  |
| 101 |  |
| 102 |  |
| 103 |  |

</p></details>
