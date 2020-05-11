import aria2p

# initialization, these are the default values
aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret="5Uj3I+RPGwZI++qmXVOAf7J57Jh2xOasZgpR807TV7Y="
    )
)

# add downloads
uris = ["https://dv98.sibnet.ru/32/28/81/3228810.mp4?st=ivxq78rmkDpoqvNl7f9DRQ&e=1585347000&stor=56&noip=1",
"https://dv98.sibnet.ru/32/28/81/3228811.mp4?st=3eu4wGqxGnW2SpR-TBEZgA&e=1585347000&stor=53&noip=1",
"https://dv98.sibnet.ru/32/32/11/3232114.mp4?st=lQM82wDFHO52tr_Xzf58LA&e=1585347000&stor=53&noip=1",
"https://dv98.sibnet.ru/32/35/51/3235516.mp4?st=5a0p3Lsx9K6HN29hKRg3Kg&e=1585347000&stor=25&noip=1",
"https://dv98.sibnet.ru/32/39/35/3239350.mp4?st=4eYSm1X3DXC5b6E4VaRrag&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/32/43/46/3243466.mp4?st=Vlu_pW_iD7690gtj5M_L2Q&e=1585347000&stor=25&noip=1",
"https://dv98.sibnet.ru/32/46/78/3246781.mp4?st=5EVsQUYQiyJowUa_ZlueTw&e=1585347000&stor=56&noip=1",
"https://dv98.sibnet.ru/32/50/11/3250118.mp4?st=y6dtkfUrnbRPOrtQxsilIA&e=1585347000&stor=53&noip=1",
"https://dv98.sibnet.ru/32/53/46/3253460.mp4?st=oruky-w9Oxj-VNHTvvQBZQ&e=1585347000&stor=6&noip=1",
"https://dv98.sibnet.ru/32/56/93/3256938.mp4?st=edsnQNjp-op_99emq0-v3w&e=1585347000&stor=56&noip=1",
"https://dv98.sibnet.ru/32/60/60/3260609.mp4?st=8-dj5GVbeeWnKb9Cwa9_4Q&e=1585347000&stor=56&noip=1",
"https://dv98.sibnet.ru/32/63/93/3263932.mp4?st=Zds66enAvN6bU4_xg6q_QQ&e=1585347000&stor=58&noip=1",
"https://dv98.sibnet.ru/32/67/78/3267784.mp4?st=nLQFv1Sehmp0HTNm1KaNYQ&e=1585347000&stor=53&noip=1",
"https://dv98.sibnet.ru/32/75/11/3275116.mp4?st=3CwT8y0IH_cBcR8L9615Ug&e=1585347000&stor=6&noip=1",
"https://dv98.sibnet.ru/32/80/04/3280049.mp4?st=EHYiknNl5GlgAFhhwX9SRQ&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/32/84/20/3284201.mp4?st=bdkooktQPMzi9gfXBBunkw&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/32/88/61/3288612.mp4?st=NCwgyH1hDlP0qqro3m9ifA&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/32/92/20/3292200.mp4?st=nXVtvC45BvstxwYwcFHzQg&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/32/96/48/3296488.mp4?st=1JGt_KRSniaiMk_IPUgu7A&e=1585347000&stor=26&noip=1",
"https://dv98.sibnet.ru/33/00/36/3300369.mp4?st=sj4XPXyejYuH8Ghy7qnYSg&e=1585347000&stor=47&noip=1",
"https://dv98.sibnet.ru/33/04/44/3304444.mp4?st=gM3MPLnTCrEXnA7BB-vGDQ&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/33/09/25/3309251.mp4?st=uv0ie6jmRe347vNjdPlpJA&e=1585347000&stor=46&noip=1",
"https://dv98.sibnet.ru/33/13/24/3313244.mp4?st=UrGiJHEmPcXxg4QmXu7hig&e=1585347000&stor=10&noip=1",
"https://dv98.sibnet.ru/33/18/09/3318096.mp4?st=oLsbcY2MTEN7Zgzoy8dHsQ&e=1585347000&stor=58&noip=1",
"https://dv98.sibnet.ru/33/22/89/3322890.mp4?st=Pp7URAcEdwDTIQ6uFvIwDg&e=1585347000&stor=46&noip=1"]

download = aria2.add_uris(uris)

# list downloads
#downloads = aria2.get_downloads()

#for download in downloads:
#    print(download.name, download.download_speed, download.status)
