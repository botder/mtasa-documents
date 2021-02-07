# libmysql.dll

## Imports

<details><summary><b>KERNEL32.dll</b> (144)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 317 | FlsAlloc |
| 673 | HeapFree |
| 1061 | Sleep |
| 505 | GetModuleHandleW |
| 544 | GetProcAddress |
| 261 | ExitProcess |
| 1004 | SetHandleCount |
| 571 | GetStdHandle |
| 472 | GetFileType |
| 569 | GetStartupInfoA |
| 191 | DeleteCriticalSection |
| 500 | GetModuleFileNameA |
| 331 | FreeEnvironmentStringsA |
| 448 | GetEnvironmentStrings |
| 332 | FreeEnvironmentStringsW |
| 1150 | WideCharToMultiByte |
| 450 | GetEnvironmentStringsW |
| 677 | HeapSetInformation |
| 671 | HeapCreate |
| 672 | HeapDestroy |
| 918 | RtlUnwindEx |
| 846 | QueryPerformanceCounter |
| 614 | GetTickCount |
| 427 | GetCurrentProcessId |
| 591 | GetSystemTimeAsFileTime |
| 745 | LeaveCriticalSection |
| 268 | FatalAppExitA |
| 218 | EnterCriticalSection |
| 348 | GetCPInfo |
| 339 | GetACP |
| 531 | GetOEMCP |
| 725 | IsValidCodePage |
| 669 | HeapAlloc |
| 676 | HeapReAlloc |
| 1169 | WriteFile |
| 1073 | TerminateProcess |
| 426 | GetCurrentProcess |
| 1090 | UnhandledExceptionFilter |
| 1049 | SetUnhandledExceptionFilter |
| 715 | IsDebuggerPresent |
| 919 | RtlVirtualUnwind |
| 912 | RtlLookupFunctionEntry |
| 905 | RtlCaptureContext |
| 940 | SetConsoleCtrlHandler |
| 333 | FreeLibrary |
| 747 | LoadLibraryA |
| 693 | InitializeCriticalSectionAndSpinCount |
| 431 | GetDateFormatA |
| 616 | GetTimeFormatA |
| 621 | GetUserDefaultLCID |
| 488 | GetLocaleInfoA |
| 249 | EnumSystemLocalesA |
| 727 | IsValidLocale |
| 573 | GetStringTypeA |
| 788 | MultiByteToWideChar |
| 576 | GetStringTypeW |
| 731 | LCMapStringA |
| 733 | LCMapStringW |
| 678 | HeapSize |
| 490 | GetLocaleInfoW |
| 619 | GetTimeZoneInformation |
| 82 | CompareStringA |
| 85 | CompareStringW |
| 981 | SetEnvironmentVariableA |
| 429 | GetCurrentThread |
| 486 | GetLastError |
| 1008 | SetLastError |
| 318 | FlsFree |
| 319 | FlsGetValue |
| 1078 | TlsAlloc |
| 184 | DecodePointer |
| 214 | EncodePointer |
| 692 | InitializeCriticalSection |
| 328 | FormatMessageA |
| 748 | LoadLibraryExA |
| 388 | GetConsoleCP |
| 67 | CloseHandle |
| 1017 | SetNamedPipeHandleState |
| 1134 | WaitNamedPipeA |
| 121 | CreateFileA |
| 1093 | UnmapViewOfFile |
| 1128 | WaitForSingleObject |
| 984 | SetEvent |
| 772 | MapViewOfFile |
| 805 | OpenFileMappingA |
| 801 | OpenEventA |
| 115 | CreateEventA |
| 1126 | WaitForMultipleObjects |
| 51 | CancelIo |
| 532 | GetOverlappedResult |
| 866 | ReadFile |
| 824 | PeekNamedPipe |
| 206 | DisconnectNamedPipe |
| 847 | QueryPerformanceFrequency |
| 1079 | TlsFree |
| 1080 | TlsGetValue |
| 1081 | TlsSetValue |
| 458 | GetFileAttributesA |
| 477 | GetFullPathNameA |
| 691 | InitializeConditionVariable |
| 1136 | WakeAllConditionVariable |
| 1137 | WakeConditionVariable |
| 1062 | SleepConditionVariableCS |
| 997 | SetFilePointerEx |
| 978 | SetEndOfFile |
| 470 | GetFileSizeEx |
| 213 | DuplicateHandle |
| 459 | GetFileAttributesExA |
| 322 | FlushFileBuffers |
| 1085 | TryEnterCriticalSection |
| 817 | OpenThread |
| 1074 | TerminateThread |
| 493 | GetLogicalDrives |
| 581 | GetSystemDirectoryA |
| 502 | GetModuleHandleA |
| 640 | GetWindowsDirectoryA |
| 282 | FindClose |
| 303 | FindNextFileA |
| 286 | FindFirstFileA |
| 855 | ReadConsoleInputA |
| 956 | SetConsoleMode |
| 406 | GetConsoleMode |
| 822 | PeekConsoleInputA |
| 529 | GetNumberOfConsoleInputEvents |
| 1024 | SetStdHandle |
| 273 | FileTimeToSystemTime |
| 272 | FileTimeToLocalFileTime |
| 465 | GetFileInformationByHandle |
| 443 | GetDriveTypeA |
| 262 | ExitThread |
| 163 | CreateThread |
| 424 | GetCurrentDirectoryA |
| 971 | SetCurrentDirectoryA |
| 996 | SetFilePointer |
| 852 | RaiseException |
| 914 | RtlPcToFileHeader |
| 1158 | WriteConsoleA |
| 410 | GetConsoleOutputCP |
| 1168 | WriteConsoleW |
| 547 | GetProcessHeap |
| 368 | GetCommandLineA |
| 320 | FlsSetValue |
| 430 | GetCurrentThreadId |
| 982 | SetEnvironmentVariableW |

</p></details>
<details><summary><b>Secur32.dll</b> (7)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 30 | GetUserNameExW |
| 25 | FreeCredentialsHandle |
| 17 | DeleteSecurityContext |
| 1 | AcquireCredentialsHandleA |
| 24 | FreeContextBuffer |
| 12 | CompleteAuthToken |
| 37 | InitializeSecurityContextW |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (10)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 340 | GetTokenInformation |
| 587 | RegEnumValueA |
| 554 | RegCloseKey |
| 172 | CryptAcquireContextA |
| 199 | CryptReleaseContext |
| 189 | CryptGenRandom |
| 384 | IsValidSid |
| 258 | EqualSid |
| 393 | LookupAccountNameW |
| 602 | RegOpenKeyExA |

</p></details>
<details><summary><b>WS2_32.dll</b> (25)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 55 |  |
| 6 |  |
| 3 |  |
| 2 |  |
| 111 |  |
| 23 |  |
| 151 | freeaddrinfo |
| 152 | getaddrinfo |
| 15 |  |
| 5 |  |
| 19 |  |
| 16 |  |
| 7 |  |
| 21 |  |
| 22 |  |
| 54 | WSAIoctl |
| 10 |  |
| 151 |  |
| 112 |  |
| 18 |  |
| 156 | getnameinfo |
| 8 |  |
| 116 |  |
| 115 |  |
| 4 |  |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |
| 1 | get_tty_password |
| 2 | handle_options |
| 3 | load_defaults |
| 4 | my_init |
| 5 | myodbc_remove_escape |
| 6 | mysql_affected_rows |
| 7 | mysql_autocommit |
| 8 | mysql_change_user |
| 9 | mysql_character_set_name |
| 10 | mysql_client_find_plugin |
| 11 | mysql_client_register_plugin |
| 12 | mysql_close |
| 13 | mysql_commit |
| 14 | mysql_data_seek |
| 15 | mysql_debug |
| 16 | mysql_dump_debug_info |
| 17 | mysql_embedded |
| 18 | mysql_eof |
| 19 | mysql_errno |
| 20 | mysql_error |
| 21 | mysql_escape_string |
| 22 | mysql_fetch_field |
| 23 | mysql_fetch_field_direct |
| 24 | mysql_fetch_fields |
| 25 | mysql_fetch_lengths |
| 26 | mysql_fetch_row |
| 27 | mysql_field_count |
| 28 | mysql_field_seek |
| 29 | mysql_field_tell |
| 30 | mysql_free_result |
| 31 | mysql_get_character_set_info |
| 32 | mysql_get_client_info |
| 33 | mysql_get_client_version |
| 34 | mysql_get_host_info |
| 35 | mysql_get_option |
| 36 | mysql_get_proto_info |
| 37 | mysql_get_server_info |
| 38 | mysql_get_server_version |
| 39 | mysql_get_ssl_cipher |
| 40 | mysql_hex_string |
| 41 | mysql_info |
| 42 | mysql_init |
| 43 | mysql_insert_id |
| 44 | mysql_kill |
| 45 | mysql_list_dbs |
| 46 | mysql_list_fields |
| 47 | mysql_list_processes |
| 48 | mysql_list_tables |
| 49 | mysql_load_plugin |
| 50 | mysql_load_plugin_v |
| 51 | mysql_more_results |
| 52 | mysql_next_result |
| 53 | mysql_num_fields |
| 54 | mysql_num_rows |
| 55 | mysql_options |
| 56 | mysql_options4 |
| 57 | mysql_ping |
| 58 | mysql_plugin_options |
| 59 | mysql_query |
| 60 | mysql_read_query_result |
| 61 | mysql_real_connect |
| 62 | mysql_real_escape_string |
| 63 | mysql_real_query |
| 64 | mysql_refresh |
| 65 | mysql_reset_connection |
| 66 | mysql_rollback |
| 67 | mysql_row_seek |
| 68 | mysql_row_tell |
| 69 | mysql_select_db |
| 70 | mysql_send_query |
| 71 | mysql_server_end |
| 72 | mysql_server_init |
| 73 | mysql_set_character_set |
| 74 | mysql_set_local_infile_default |
| 75 | mysql_set_local_infile_handler |
| 76 | mysql_set_server_option |
| 77 | mysql_shutdown |
| 78 | mysql_sqlstate |
| 79 | mysql_ssl_set |
| 80 | mysql_stat |
| 81 | mysql_stmt_affected_rows |
| 82 | mysql_stmt_attr_get |
| 83 | mysql_stmt_attr_set |
| 84 | mysql_stmt_bind_param |
| 85 | mysql_stmt_bind_result |
| 86 | mysql_stmt_close |
| 87 | mysql_stmt_data_seek |
| 88 | mysql_stmt_errno |
| 89 | mysql_stmt_error |
| 90 | mysql_stmt_execute |
| 91 | mysql_stmt_fetch |
| 92 | mysql_stmt_fetch_column |
| 93 | mysql_stmt_field_count |
| 94 | mysql_stmt_free_result |
| 95 | mysql_stmt_init |
| 96 | mysql_stmt_insert_id |
| 97 | mysql_stmt_next_result |
| 98 | mysql_stmt_num_rows |
| 99 | mysql_stmt_param_count |
| 100 | mysql_stmt_param_metadata |
| 101 | mysql_stmt_prepare |
| 102 | mysql_stmt_reset |
| 103 | mysql_stmt_result_metadata |
| 104 | mysql_stmt_row_seek |
| 105 | mysql_stmt_row_tell |
| 106 | mysql_stmt_send_long_data |
| 107 | mysql_stmt_sqlstate |
| 108 | mysql_stmt_store_result |
| 109 | mysql_store_result |
| 110 | mysql_thread_end |
| 111 | mysql_thread_id |
| 112 | mysql_thread_init |
| 113 | mysql_thread_safe |
| 114 | mysql_use_result |
| 115 | mysql_warning_count |

</p></details>
