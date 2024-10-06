URL_str = input("Zadaj URL adresu: ")

# https://h.xyz/
if URL_str[:5] == "https":
    print("a) https")
    URL_protocol = URL_str[:5]
else:
    print("a) http")
    URL_protocol = URL_str[ :4 ]

for i in range(len(URL_str)):
    if URL_str[ -i ] == ".":
        H_domain_start = -i +1
        for i2 in range(len(URL_str) - 7):
            check_URL_str = URL_str[H_domain_start +i2 ]
            if URL_str[H_domain_start +i2 ] == "/":
                H_domain_end = H_domain_start + i2
                print(f"Domena najvyššej úrovne: .{URL_str[H_domain_start : H_domain_end ]}")
                break
            elif i2 == len(URL_str) - 8:
                print(f"Domena najvyššej úrovne: .{URL_str[H_domain_start:]}")
        break
            

print(f"c) {URL_str[len(URL_protocol) + 3 :H_domain_start - 1 ]} ")

        