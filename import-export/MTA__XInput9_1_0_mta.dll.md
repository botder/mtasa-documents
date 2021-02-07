# XInput9_1_0_mta.dll

## Imports

<details><summary><b>ntdll.dll</b> (1)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 918 | RtlUnwind |

</p></details>
<details><summary><b>KERNEL32.dll</b> (68)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 600 | LocalAlloc |
| 597 | LoadLibraryW |
| 248 | FreeLibrary |
| 416 | GetProcAddress |
| 369 | GetLastError |
| 86 | CreateFileW |
| 138 | DeviceIoControl |
| 675 | QueryPerformanceCounter |
| 479 | GetTickCount |
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
| 804 | SetHandleCount |
| 441 | GetStdHandle |
| 358 | GetFileType |
| 439 | GetStartupInfoA |
| 381 | GetModuleFileNameA |
| 532 | HeapDestroy |
| 530 | HeapCreate |
| 322 | GetCurrentProcess |
| 246 | FreeEnvironmentStringsA |
| 341 | GetEnvironmentStrings |
| 247 | FreeEnvironmentStringsW |
| 147 | DuplicateHandle |
| 343 | GetEnvironmentStringsW |
| 932 | WriteFile |
| 553 | InterlockedExchange |
| 904 | VirtualQuery |
| 854 | Sleep |
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
| 580 | LCMapStringA |
| 581 | LCMapStringW |
| 442 | GetStringTypeA |
| 445 | GetStringTypeW |
| 823 | SetStdHandle |
| 372 | GetLocaleInfoA |
| 902 | VirtualProtect |
| 453 | GetSystemInfo |
| 238 | FlushFileBuffers |
| 604 | LocalFree |
| 52 | CloseHandle |
| 593 | LeaveCriticalSection |
| 152 | EnterCriticalSection |
| 129 | DeleteCriticalSection |
| 547 | InitializeCriticalSection |
| 899 | VirtualFree |
| 916 | WideCharToMultiByte |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (9)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 633 | TraceMessage |
| 285 | GetTraceLoggerHandle |
| 284 | GetTraceEnableLevel |
| 283 | GetTraceEnableFlags |
| 466 | RegCreateKeyExW |
| 517 | RegSetValueExW |
| 459 | RegCloseKey |
| 642 | UnregisterTraceGuids |
| 529 | RegisterTraceGuidsW |

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
| 2 | XInputGetCapabilities |
| 3 | XInputGetDSoundAudioDeviceGuids |
| 4 | XInputGetState |
| 5 | XInputSetState |

</p></details>
