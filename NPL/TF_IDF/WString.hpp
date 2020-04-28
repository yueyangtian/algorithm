#ifndef __WSTRING_HPP__
#define __WSTRING_HPP__
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <locale>


void Split(const std::wstring &s, wchar_t delim, std::vector<std::wstring> &elems) 
{
    std::wstringstream ss;
    ss.str(s);
    std::wstring item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
}
std::vector<std::wstring> Split(const std::wstring &s, wchar_t delim) 
{
    std::vector<std::wstring> elems;
    Split(s, delim, elems);
    return elems;
}
int test_split()
{
    std::locale::global(std::locale("zh_CN.utf8"));
    std::wstring s = L"雷军 拿 融资 隔 空 喊话 周鸿 搜狐 财经";
    std::vector<std::wstring> v = Split(s, L' ');
    for(int i = 0; i < v.size(); ++i)
    {
        std::wcout << v[i] <<std::endl;
    }
    return 0;
}


#endif //__WSTRING_HPP__
