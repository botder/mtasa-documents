# Uninstall.exe

## Imports

<details><summary><b>KERNEL32.dll</b> (70)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 1130 | SetFileTime |
| 96 | CompareFileTime |
| 1053 | SearchPathW |
| 609 | GetShortPathNameW |
| 507 | GetFullPathNameW |
| 867 | MoveFileW |
| 1101 | SetCurrentDirectoryW |
| 490 | GetFileAttributesW |
| 514 | GetLastError |
| 129 | CreateDirectoryW |
| 1121 | SetFileAttributesW |
| 1202 | Sleep |
| 659 | GetTickCount |
| 143 | CreateFileW |
| 496 | GetFileSize |
| 532 | GetModuleFileNameW |
| 448 | GetCurrentProcess |
| 117 | CopyFileW |
| 281 | ExitProcess |
| 687 | GetWindowsDirectoryW |
| 645 | GetTempPathW |
| 391 | GetCommandLineW |
| 1112 | SetErrorMode |
| 82 | CloseHandle |
| 1358 | lstrlenW |
| 1355 | lstrcpynW |
| 463 | GetDiskFreeSpaceW |
| 709 | GlobalUnlock |
| 702 | GlobalLock |
| 181 | CreateThread |
| 831 | LoadLibraryW |
| 168 | CreateProcessW |
| 1348 | lstrcmpiA |
| 643 | GetTempFileNameW |
| 1343 | lstrcatW |
| 581 | GetProcAddress |
| 828 | LoadLibraryA |
| 533 | GetModuleHandleA |
| 896 | OpenProcess |
| 1352 | lstrcpyW |
| 676 | GetVersionExW |
| 624 | GetSystemDirectoryW |
| 674 | GetVersion |
| 1351 | lstrcpyA |
| 1027 | RemoveDirectoryW |
| 1345 | lstrcmpA |
| 1349 | lstrcmpiW |
| 1346 | lstrcmpW |
| 285 | ExpandEnvironmentStringsW |
| 691 | GlobalAlloc |
| 1273 | WaitForSingleObject |
| 479 | GetExitCodeProcess |
| 698 | GlobalFree |
| 536 | GetModuleHandleW |
| 830 | LoadLibraryExW |
| 354 | FreeLibrary |
| 1323 | WritePrivateProfileStringW |
| 578 | GetPrivateProfileStringW |
| 1297 | WideCharToMultiByte |
| 1357 | lstrlenA |
| 870 | MulDiv |
| 1317 | WriteFile |
| 960 | ReadFile |
| 871 | MultiByteToWideChar |
| 1126 | SetFilePointer |
| 302 | FindClose |
| 325 | FindNextFileW |
| 313 | FindFirstFileW |
| 214 | DeleteFileW |
| 1354 | lstrcpynA |

</p></details>
<details><summary><b>USER32.dll</b> (68)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 263 | GetAsyncKeyState |
| 462 | IsDlgButtonChecked |
| 621 | ScreenToClient |
| 347 | GetMessagePos |
| 30 | CallWindowProcW |
| 480 | IsWindowVisible |
| 487 | LoadBitmapW |
| 73 | CloseClipboard |
| 646 | SetClipboardData |
| 213 | EmptyClipboard |
| 550 | OpenClipboard |
| 758 | TrackPopupMenu |
| 412 | GetWindowRect |
| 10 | AppendMenuW |
| 107 | CreatePopupMenu |
| 382 | GetSystemMetrics |
| 218 | EndDialog |
| 214 | EnableMenuItem |
| 381 | GetSystemMenu |
| 644 | SetClassLongW |
| 476 | IsWindowEnabled |
| 710 | SetWindowPos |
| 172 | DialogBoxParamW |
| 62 | CheckDlgButton |
| 110 | CreateWindowExW |
| 748 | SystemParametersInfoW |
| 590 | RegisterClassW |
| 656 | SetDlgItemTextW |
| 298 | GetDlgItemTextW |
| 530 | MessageBoxIndirectW |
| 47 | CharNextA |
| 60 | CharUpperW |
| 52 | CharPrevW |
| 821 | wvsprintfW |
| 175 | DispatchMessageW |
| 563 | PeekMessageW |
| 818 | wsprintfA |
| 166 | DestroyWindow |
| 99 | CreateDialogParamW |
| 699 | SetTimer |
| 715 | SetWindowTextW |
| 567 | PostQuitMessage |
| 659 | SetForegroundWindow |
| 735 | ShowWindow |
| 819 | wsprintfW |
| 635 | SendMessageTimeoutW |
| 491 | LoadCursorW |
| 648 | SetCursor |
| 406 | GetWindowLongW |
| 379 | GetSysColor |
| 49 | CharNextW |
| 270 | GetClassInfoW |
| 245 | ExitWindowsEx |
| 475 | IsWindow |
| 295 | GetDlgItem |
| 708 | SetWindowLongW |
| 495 | LoadImageW |
| 289 | GetDC |
| 216 | EnableWindow |
| 446 | InvalidateRect |
| 636 | SendMessageW |
| 156 | DefWindowProcW |
| 14 | BeginPaint |
| 276 | GetClientRect |
| 246 | FillRect |
| 208 | DrawTextW |
| 220 | EndPaint |
| 249 | FindWindowExW |

</p></details>
<details><summary><b>GDI32.dll</b> (8)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 638 | SetBkColor |
| 459 | GetDeviceCaps |
| 230 | DeleteObject |
| 44 | CreateBrushIndirect |
| 64 | CreateFontIndirectW |
| 639 | SetBkMode |
| 678 | SetTextColor |
| 631 | SelectObject |

</p></details>
<details><summary><b>SHELL32.dll</b> (6)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 123 | SHBrowseForFolderW |
| 215 | SHGetPathFromIDListW |
| 189 | SHGetFileInfoW |
| 290 | ShellExecuteW |
| 172 | SHFileOperationW |
| 223 | SHGetSpecialFolderLocation |

</p></details>
<details><summary><b>ADVAPI32.dll</b> (9)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 592 | RegEnumKeyW |
| 609 | RegOpenKeyExW |
| 560 | RegCloseKey |
| 580 | RegDeleteKeyW |
| 584 | RegDeleteValueW |
| 569 | RegCreateKeyExW |
| 638 | RegSetValueExW |
| 622 | RegQueryValueExW |
| 594 | RegEnumValueW |

</p></details>
<details><summary><b>COMCTL32.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 79 | ImageList_AddMasked |
| 84 | ImageList_Destroy |
| 17 |  |
| 83 | ImageList_Create |

</p></details>
<details><summary><b>ole32.dll</b> (4)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 104 | CoTaskMemFree |
| 306 | OleInitialize |
| 329 | OleUninitialize |
| 16 | CoCreateInstance |

</p></details>
<details><summary><b>VERSION.dll</b> (3)</summary><p>

| Ordinal | Name |
| ------- | ---- |
| 5 | GetFileVersionInfoSizeW |
| 6 | GetFileVersionInfoW |
| 14 | VerQueryValueW |

</p></details>

## Exports


| Ordinal | Name |
| ------- | ---- |

</p></details>
