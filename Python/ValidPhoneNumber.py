# 手机号码校验

# 校验准则 移动，联通，电信
CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184,  187, 188, 147, 178, 1705] 
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709] 
CN_telecom = [133, 153, 180, 181, 189, 177, 1700]


# 校验长度是否符合
def valid_length(num):
    if len(num) == 11:
        return True
    else:
        return False


# 验证num个字符
def valid_num_n(tell_num, valid_num):
    num = int(tell_num[0: valid_num])
    if num in CN_mobile:
        return "中国移动"
    elif num in CN_union:
        return "中国联通"
    elif num in CN_telecom:
        return "中国电信"
    else:
        return False


# 校验是否符合规范,辨别号码类型
def valid_type(num):
    num_3 = valid_num_n(num, 3)
    num_4 = valid_num_n(num, 4)
    if (not num_3) & (not num_4):# 3,4个字符串都没有找到
        return "手机号错误"
    elif num_3:
        return num_3
    else:
        return num_4


# 主函数
def valid_main():
    phone_number = str(input("请输入你的手机号码："))
    if valid_length(phone_number):
        result = valid_type(phone_number)
        if result == "手机号错误":
            print (result)
            valid_main()
        else:
            print ("号段：" + result + "\n我们将将验证码发送到" + phone_number + "，请查收~")
            return
    else:
        print ("您输入的手机号不是11位！")
        valid_main()

valid_main()
