#include "WString.hpp"
#include <fstream>
int main()
{
    std::locale::global(std::locale("zh_CN.utf8"));
    std::wifstream fs("./data/allfiles/1111business.seg.cln.txt",  std::ios::binary);
    while(!fs.eof())
    {
        std::wstring s ;
        fs >> s;
        std::wcout << s << L"--";
    }
    return 0;
}
