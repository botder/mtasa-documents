# libmysql.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (153)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 285 | FindFirstFileA |
| 852 | QueryPerformanceCounter |
| 853 | QueryPerformanceFrequency |
| 429 | GetCurrentThreadId |
| 751 | LeaveCriticalSection |
| 217 | EnterCriticalSection |
| 488 | GetLocaleInfoA |
| 502 | GetModuleHandleA |
| 500 | GetModuleFileNameA |
| 640 | GetWindowsDirectoryA |
| 1057 | Sleep |
| 190 | DeleteCriticalSection |
| 692 | InitializeCriticalSection |
| 704 | InterlockedIncrement |
| 600 | GetTempFileNameA |
| 602 | GetTempPathA |
| 458 | GetFileAttributesExA |
| 139 | CreateMutexA |
| 887 | ReleaseMutex |
| 860 | ReadConsoleA |
| 411 | GetConsoleScreenBufferInfo |
| 571 | GetStdHandle |
| 951 | SetConsoleMode |
| 405 | GetConsoleMode |
| 426 | GetCurrentProcessId |
| 192 | DeleteFileA |
| 785 | MoveFileA |
| 614 | GetTickCount |
| 591 | GetSystemTimeAsFileTime |
| 774 | LockFileEx |
| 1004 | SetLastError |
| 302 | FindNextFileA |
| 121 | CreateFileMappingA |
| 324 | FlushViewOfFile |
| 457 | GetFileAttributesA |
| 1075 | TlsFree |
| 1076 | TlsGetValue |
| 1077 | TlsSetValue |
| 1074 | TlsAlloc |
| 114 | CreateEventA |
| 906 | ResetEvent |
| 1122 | WaitForMultipleObjects |
| 872 | ReadFile |
| 1165 | WriteFile |
| 992 | SetFilePointerEx |
| 973 | SetEndOfFile |
| 469 | GetFileSizeEx |
| 212 | DuplicateHandle |
| 425 | GetCurrentProcess |
| 321 | FlushFileBuffers |
| 628 | GetVersion |
| 1081 | TryEnterCriticalSection |
| 823 | OpenThread |
| 783 | Module32Next |
| 781 | Module32First |
| 172 | CreateToolhelp32Snapshot |
| 428 | GetCurrentThread |
| 585 | GetSystemInfo |
| 1065 | SwitchToThread |
| 108 | CreateDirectoryA |
| 983 | SetFileAttributesA |
| 547 | GetProcessHeap |
| 858 | RaiseException |
| 281 | FindClose |
| 807 | OpenEventA |
| 811 | OpenFileMappingA |
| 778 | MapViewOfFile |
| 979 | SetEvent |
| 1124 | WaitForSingleObject |
| 1089 | UnmapViewOfFile |
| 486 | GetLastError |
| 120 | CreateFileA |
| 1130 | WaitNamedPipeA |
| 1013 | SetNamedPipeHandleState |
| 67 | CloseHandle |
| 581 | GetSystemDirectoryA |
| 753 | LoadLibraryA |
| 332 | FreeLibrary |
| 1088 | UnlockFileEx |
| 544 | GetProcAddress |
| 409 | GetConsoleOutputCP |
| 1154 | WriteConsoleA |
| 977 | SetEnvironmentVariableW |
| 490 | GetLocaleInfoW |
| 976 | SetEnvironmentVariableA |
| 85 | CompareStringW |
| 82 | CompareStringA |
| 733 | IsValidLocale |
| 248 | EnumSystemLocalesA |
| 621 | GetUserDefaultLCID |
| 430 | GetDateFormatA |
| 616 | GetTimeFormatA |
| 576 | GetStringTypeW |
| 573 | GetStringTypeA |
| 739 | LCMapStringW |
| 737 | LCMapStringA |
| 449 | GetEnvironmentStringsW |
| 331 | FreeEnvironmentStringsW |
| 447 | GetEnvironmentStrings |
| 330 | FreeEnvironmentStringsA |
| 966 | SetCurrentDirectoryA |
| 423 | GetCurrentDirectoryA |
| 678 | HeapSize |
| 756 | LoadLibraryW |
| 914 | RtlUnwind |
| 673 | HeapFree |
| 505 | GetModuleHandleW |
| 260 | ExitProcess |
| 861 | ReadConsoleInputA |
| 828 | PeekConsoleInputA |
| 529 | GetNumberOfConsoleInputEvents |
| 935 | SetConsoleCtrlHandler |
| 669 | HeapAlloc |
| 1164 | WriteConsoleW |
| 471 | GetFileType |
| 501 | GetModuleFileNameW |
| 1086 | UnhandledExceptionFilter |
| 1045 | SetUnhandledExceptionFilter |
| 995 | SetFileTime |
| 763 | LocalFileTimeToFileTime |
| 1066 | SystemTimeToFileTime |
| 1146 | WideCharToMultiByte |
| 619 | GetTimeZoneInformation |
| 1069 | TerminateProcess |
| 721 | IsDebuggerPresent |
| 272 | FileTimeToSystemTime |
| 271 | FileTimeToLocalFileTime |
| 676 | HeapReAlloc |
| 442 | GetDriveTypeA |
| 1020 | SetStdHandle |
| 464 | GetFileInformationByHandle |
| 830 | PeekNamedPipe |
| 261 | ExitThread |
| 163 | CreateThread |
| 476 | GetFullPathNameA |
| 367 | GetCommandLineA |
| 671 | HeapCreate |
| 672 | HeapDestroy |
| 1111 | VirtualFree |
| 267 | FatalAppExitA |
| 1108 | VirtualAlloc |
| 347 | GetCPInfo |
| 700 | InterlockedDecrement |
| 338 | GetACP |
| 531 | GetOEMCP |
| 731 | IsValidCodePage |
| 701 | InterlockedExchange |
| 693 | InitializeCriticalSectionAndSpinCount |
| 1000 | SetHandleCount |
| 569 | GetStartupInfoA |
| 387 | GetConsoleCP |
| 794 | MultiByteToWideChar |
| 991 | SetFilePointer |

</p></details>
<details><summary><b>USER32.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 670 | SetTimer |
| 539 | PeekMessageA |
| 461 | KillTimer |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (16)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 497 | OpenProcessToken |
| 340 | GetTokenInformation |
| 384 | IsValidSid |
| 304 | GetLengthSid |
| 368 | InitializeAcl |
| 16 | AddAccessAllowedAce |
| 369 | InitializeSecurityDescriptor |
| 688 | SetSecurityDescriptorDacl |
| 282 | FreeSid |
| 602 | RegOpenKeyExA |
| 587 | RegEnumValueA |
| 554 | RegCloseKey |
| 189 | CryptGenRandom |
| 199 | CryptReleaseContext |
| 172 | CryptAcquireContextA |
| 31 | AllocateAndInitializeSid |

</p></details>
<details><summary><b>WS2_32.dll</b> (24)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 116 |  |
| 16 |  |
| 22 |  |
| 19 |  |
| 10 |  |
| 18 |  |
| 151 |  |
| 23 |  |
| 3 |  |
| 115 |  |
| 112 |  |
| 15 |  |
| 56 |  |
| 51 |  |
| 9 |  |
| 55 |  |
| 8 |  |
| 12 |  |
| 111 |  |
| 11 |  |
| 21 |  |
| 5 |  |
| 4 |  |
| 52 |  |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | myodbc_remove_escape |
| 2 | mysql_affected_rows |
| 3 | mysql_autocommit |
| 4 | mysql_change_user |
| 5 | mysql_character_set_name |
| 6 | mysql_close |
| 7 | mysql_commit |
| 8 | mysql_data_seek |
| 9 | mysql_debug |
| 10 | mysql_dump_debug_info |
| 11 | mysql_embedded |
| 12 | mysql_eof |
| 13 | mysql_errno |
| 14 | mysql_error |
| 15 | mysql_escape_string |
| 16 | mysql_fetch_field |
| 17 | mysql_fetch_field_direct |
| 18 | mysql_fetch_fields |
| 19 | mysql_fetch_lengths |
| 20 | mysql_fetch_row |
| 21 | mysql_field_count |
| 22 | mysql_field_seek |
| 23 | mysql_field_tell |
| 24 | mysql_free_result |
| 25 | mysql_get_character_set_info |
| 26 | mysql_get_client_info |
| 27 | mysql_get_client_version |
| 28 | mysql_get_host_info |
| 29 | mysql_get_parameters |
| 30 | mysql_get_proto_info |
| 31 | mysql_get_server_info |
| 32 | mysql_get_server_version |
| 33 | mysql_get_ssl_cipher |
| 34 | mysql_hex_string |
| 35 | mysql_info |
| 36 | mysql_init |
| 37 | mysql_insert_id |
| 38 | mysql_kill |
| 39 | mysql_list_dbs |
| 40 | mysql_list_fields |
| 41 | mysql_list_processes |
| 42 | mysql_list_tables |
| 43 | mysql_more_results |
| 44 | mysql_next_result |
| 45 | mysql_num_fields |
| 46 | mysql_num_rows |
| 47 | mysql_options |
| 48 | mysql_ping |
| 49 | mysql_query |
| 50 | mysql_read_query_result |
| 51 | mysql_real_connect |
| 52 | mysql_real_escape_string |
| 53 | mysql_real_query |
| 54 | mysql_refresh |
| 55 | mysql_rollback |
| 56 | mysql_row_seek |
| 57 | mysql_row_tell |
| 58 | mysql_select_db |
| 59 | mysql_send_query |
| 60 | mysql_server_end |
| 61 | mysql_server_init |
| 62 | mysql_set_character_set |
| 63 | mysql_set_local_infile_default |
| 64 | mysql_set_local_infile_handler |
| 65 | mysql_set_server_option |
| 66 | mysql_shutdown |
| 67 | mysql_sqlstate |
| 68 | mysql_ssl_set |
| 69 | mysql_stat |
| 70 | mysql_stmt_affected_rows |
| 71 | mysql_stmt_attr_get |
| 72 | mysql_stmt_attr_set |
| 73 | mysql_stmt_bind_param |
| 74 | mysql_stmt_bind_result |
| 75 | mysql_stmt_close |
| 76 | mysql_stmt_data_seek |
| 77 | mysql_stmt_errno |
| 78 | mysql_stmt_error |
| 79 | mysql_stmt_execute |
| 80 | mysql_stmt_fetch |
| 81 | mysql_stmt_fetch_column |
| 82 | mysql_stmt_field_count |
| 83 | mysql_stmt_free_result |
| 84 | mysql_stmt_init |
| 85 | mysql_stmt_insert_id |
| 86 | mysql_stmt_next_result |
| 87 | mysql_stmt_num_rows |
| 88 | mysql_stmt_param_count |
| 89 | mysql_stmt_param_metadata |
| 90 | mysql_stmt_prepare |
| 91 | mysql_stmt_reset |
| 92 | mysql_stmt_result_metadata |
| 93 | mysql_stmt_row_seek |
| 94 | mysql_stmt_row_tell |
| 95 | mysql_stmt_send_long_data |
| 96 | mysql_stmt_sqlstate |
| 97 | mysql_stmt_store_result |
| 98 | mysql_store_result |
| 99 | mysql_thread_end |
| 100 | mysql_thread_id |
| 101 | mysql_thread_init |
| 102 | mysql_thread_safe |
| 103 | mysql_use_result |
| 104 | mysql_warning_count |

</p></details>
