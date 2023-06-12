Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class language:
    def __init__(self,country):
        self.country=country
        if(self.country=="India"):
                 lang_india=list()
                 req=requests.get("https://www.ethnologue.com/country/IN/")
                 soup=BeautifulSoup(req.content,"html.parser")

                 for i in soup.find_all("dt",{"class":"languages__label entry__label"}):
                      lang_india.append(i.getText().replace("\n"," "))
     
                 for i in lang_india:
                      print(i)
     
     def browse_country(self):
                country_code=list()
                req=requests.get("https://www.ethnologue.com/browse/countries/")
                soup=BeautifulSoup(req.content,"html.parser")

                for i in soup.find_all("div",{"class":"browse__countries"}):
                     for j in i.find_all("a"):
                          country_code.append((j['href'].replace('/country/'," ")))
                for i in country_code:
                     print(i)
                     
SyntaxError: unindent does not match any outer indentation level
class language:
    def __init__(self,country):
        self.country=country
        if(self.country=="India"):
            lang_india=list()
            req=requests.get("https://www.ethnologue.com/country/IN/")
            soup=BeautifulSoup(req.content,"html.parser")

            for i in soup.find_all("dt",{"class":"languages__label entry__label"}):
                lang_india.append(i.getText().replace("\n"," "))

            for i in lang_india:
                print(i)

     def browse_country(self):
                country_code=list()
                req=requests.get("https://www.ethnologue.com/browse/countries/")
                soup=BeautifulSoup(req.content,"html.parser")

                for i in soup.find_all("div",{"class":"browse__countries"}):
                     for j in i.find_all("a"):
                          country_code.append((j['href'].replace('/country/'," ")))
                for i in country_code:
                     print(i)
                     
SyntaxError: unindent does not match any outer indentation level

class language:
    def __init__(self,country):
        self.country=country
        if(self.country=="India"):
            lang_india=list()
            req=requests.get("https://www.ethnologue.com/country/IN/")
            soup=BeautifulSoup(req.content,"html.parser")

            for i in soup.find_all("dt",{"class":"languages__label entry__label"}):
                lang_india.append(i.getText().replace("\n"," "))

            for i in lang_india:
                print(i)

    def browse_country(self):
               country_code=list()
               req=requests.get("https://www.ethnologue.com/browse/countries/")
               soup=BeautifulSoup(req.content,"html.parser")

               for i in soup.find_all("div",{"class":"browse__countries"}):
                     for j in i.find_all("a"):
                          country_code.append((j['href'].replace('/country/'," ")))
               for i in country_code:
                     print(i)

                     
l=language("India")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l=language("India")
  File "<pyshell#4>", line 6, in __init__
    req=requests.get("https://www.ethnologue.com/country/IN/")
NameError: name 'requests' is not defined
import requests
from bs4 import BeautifulSoup
l=language("India")
A-Pucikwar apq
Adi adi
Adi, Galo adl
Agariya agi
Ahirani ahr
Ahom aho
Aimol aim
Aiton aio
Aka-Bea abj
Aka-Bo akm
Aka-Cari aci
Aka-Jeru akj
Aka-Kede akx
Aka-Kol aky
Aka-Kora ack
Akar-Bale acl
Allar all
Amri Karbi ajz
Anal anm
Andaman Hindi Creole hca
Andh anr
Angika anp
Apatani apt
Arabic, Mesopotamian Spoken acm
Aranadan aaf
Assamese asm
Asuri asr
Atong aot
Awadhi awa
Badaga bfq
Bagheli bfy
Bagri bgq
Bajjika vjk
Balochi, Eastern bgp
Balti bft
Bantawa bap
Bareli, Palya bpx
Bareli, Pauri bfb
Bareli, Rathwi bgd
Bateri btv
Bauria bge
Bazigar bfr
Bellari brw
Bengali ben
Bhadrawahi bhd
Bhalay bhx
Bharia bha
Bhatri bgw
Bhattiyali bht
Bhilali bhi
Bhili bhb
Bhojpuri bho
Bhunjia bhu
Biate biu
Bijori bix
Bilaspuri kfs
Birhor biy
Bishnupuriya bpy
Bodo Parja bdv
Bondo bfw
Boro brx
Braj Bhasha bra
Brokskat bkk
Bugun bgg
Buksa tkb
Bundeli bns
Burushaski bsk
Byangsi bee
Chakma ccp
Chambeali cdh
Chamling rab
Changthang cna
Chaudangsi cdn
Chaura crv
Chenchu cde
Chetti, Moundadan cty
Chetti, Wayanad ctt
Chhattisgarhi hne
Chin, Bawm bgr
Chin, Falam cfm
Chin, Hakha cnh
Chin, Khumi cnk
Chin, Mara mrh
Chin, Matu hlt
Chin, Paite pck
Chin, Tedim ctd
Chin, Thado tcz
Chin, Zyphe zyp
Chinali cih
Chinese, Mandarin cmn
Chiru cdf
Chodri cdi
Chug cvg
Churahi cdj
Dangi dhn
Darlong dln
Darmiya drd
Deccan dcc
Deori der
Desiya dso
Dhatki mki
Dhimal dhi
Dhodia dho
Dhundari dhd
Digaro-Mishmi mhu
Dimasa dis
Dogri dgo
Dogri doi
Dotyali dty
Dubli dub
Dungra Bhil duh
Duruwa pci
Dzongkha dzo
English eng
Eravallan era
French fra
Gadaba, Bodo gbj
Gadaba, Mudhili gau
Gadaba, Pottangi Ollar gdb
Gaddi gbk
Gahri bfu
Gamit gbl
Gangte gnb
Garasia, Adiwasi gas
Garasia, Rajput gra
Garhwali gbm
Garo grt
Gata’ gaq
Godwari gdx
Gondi gon
Gondi, Adilabad wsg
Gondi, Aheri esg
Gondi, Northern gno
Gowlan goj
Gowli gok
Great Andamanese, Mixed gac
Groma gro
Gujarati guj
Gujari gju
Gurung gvr
Hajong haj
Halbi hlb
Haroti hoj
Haryanvi bgc
Hindi hin
Hinduri hii
Hmar hmr
Ho hoc
Holiya hoy
Hrangkhol hra
Hruso hru
Idu-Mishmi clk
Indian Sign Language ins
Indo-Portuguese idb
Irula iru
Jad jda
Jangshung jna
Jarawa anq
Jaunsari jns
Juang jun
Juray juy
Kacchi kfr
Kachari xac
Kadar kej
Kaikadi kep
Kalanadi wkl
Kamar keq
Kamtapuri rkt
Kanashi xns
Kanauji bjj
Kangri xnr
Kanikkaran kev
Kanjari kft
Kannada kan
Karbi mjw
Kashmiri kas
Katkari kfu
Khah hkh
Khaling klr
Khamba kbg
Khamti kht
Khamyang ksu
Khandesi khn
Kharia khr
Kharia Thar ksy
Khasi kha
Khirwar kwx
Khowar khw
Kinnauri kfk
Kinnauri, Bhoti nes
Kinnauri, Chhoyul tpq
Kinnauri, Chitkuli cik
Kinnauri, Pahari kjo
Kisan xis
Koch kdq
Koda cdz
Kodaku ksz
Kodava kfa
Koireng nkd
Kok Borok trp
Kolami, Northwestern kfb
Kolami, Southeastern nit
Koli, Kachi gjk
Koli, Wadiyari kxp
Kom kmm
Konda-Dora kfc
Konkani knn
Konkani kok
Konkani, Goan gom
Koraga, Korra kfd
Koraga, Mudu vmd
Korean kor
Korku kfq
Korlai Portuguese Creole vkp
Koro jkr
Korwa kfp
Kota kfe
Koya kff
Kudiya kfg
Kudmali kyw
Kui uki
Kui, Dawik dwk
Kukna kex
Kulung kle
Kumaoni kfy
Kumarbhag Paharia kmj
Kumbaran wkb
Kunduvadi wku
Kupia key
Kurichiya kfh
Kurmukar kfv
Kurumba, Alu xua
Kurumba, Attapady pkr
Kurumba, Betta xub
Kurumba, Jennu xuj
Kurumba, Kannada kfi
Kurumba, Mullu kpb
Kurux kru
Kuvi kxv
Ladakhi lbj
Lambadi lmn
Lamkang lmk
Lepcha lep
Lhomi lhm
Limbu lif
Lish lsh
Lisu lis
Lodhi lbm
Lohar, Gade gda
Lohar, Lahul lhl
Lyngngam lyg
Magahi mag
Magar, Eastern mgp
Mahali mjx
Maithili mai
Majhi mjz
Majhwar mmj
Mal Paharia mkb
Mala Malasar ima
Malankuravan mjo
Malapandaram mjp
Malaryan mjq
Malasar ymr
Malavedan mjr
Malayalam mal
Maldivian div
Malvi mup
Manda mha
Mandeali mjl
Manna-Dora mju
Mannan mjv
Marathi mar
Maria mrr
Maria, Dandami daq
Marma rmz
Marwari mwr
Marwari rwr
Mawchi mke
Meitei mni
Merwari wry
Mewari mtr
Mewati wtm
Miji sjl
Miju-Mishmi mxj
Mirgan zrg
Mising mrg
Mizo lus
Monpa, Kalaktang kkf
Monpa, Tawang twm
Mru mro
Muduga udg
Mugom muk
Mukha-Dora mmk
Munda unx
Mundari unr
Muria, Eastern emu
Muria, Far Western fmu
Muria, Western mut
Muthuvan muv
Na nbt
Naga, Angami njm
Naga, Ao njo
Naga, Chang nbc
Naga, Chokri nri
Naga, Chothe nct
Naga, Inpui nkf
Naga, Kharam kfw
Naga, Khezha nkh
Naga, Khiamniungan kix
Naga, Khoibu nkb
Naga, Konyak nbe
Naga, Liangmai njn
Naga, Lotha njh
Naga, Makuri jmn
Naga, Mao nbi
Naga, Maram nma
Naga, Maring nng
Naga, Monsang nmh
Naga, Moyon nmo
Naga, Mzieme nme
Naga, Nocte njb
Naga, Northern Rengma nnl
Naga, Phom nph
Naga, Pochuri npo
Naga, Poumai pmx
Naga, Puimei npu
Naga, Rongmei nbu
Naga, Sangtam nsa
Naga, Southern Rengma nre
Naga, Sumi nsm
Naga, Tangkhul nmf
Naga, Tangsa nst
Naga, Tarao tro
Naga, Thangal nki
Naga, Tutsa tvt
Naga, Wancho nnp
Naga, Yimchungru yim
Naga, Zeme nzm
Nagamese nag
Nagarchal nbg
Nahali nlx
Nahari nhh
Nefamese nef
Nepali npi
Newar new
Nicobarese, Car caq
Nicobarese, Central ncb
Nicobarese, Southern nik
Nihali nll
Nimadi noe
Noiri noi
Nora nrr
Nyishi njz
Oadki odk
Odia ory
Oko-Juwoi okj
Öñge oon
Oriya ori
Oriya, Adivasi ort
Pahari-Potwari phr
Pahari, Kullu kfx
Pahari, Mahasu bfz
Pali pli
Paliyan pcf
Panchpargania tdb
Pangwali pgg
Paniya pcg
Pankhu pkh
Pardhan pch
Pardhi pcl
Parenga pcj
Pashto, Northern pbu
Pathiya pty
Pattani lae
Pattapu ptq
Pengo peg
Persian, Iranian pes
Phake phk
Phudagi phd
Pnar pbv
Portuguese por
Powari pwr
Punjabi, Eastern pan
Punjabi, Western pnb
Purig prx
Puroik suv
Purum pub
Rabha rah
Rajasthani raj
Ralte ral
Rangkas rgk
Ranglong rnl
Rathawi rtw
Ravula yea
Rawang raw
Rawat jnl
Reli rei
Riang ria
Rohingya rhg
Rongpo rnp
Ruga ruh
Sadri sck
Sakachep sch
Sambalpuri spv
Samvedi smv
Sansi ssi
Sanskrit san
Santhali sat
Saraiki skr
Sartang onp
Sauria Paharia mjt
Sentinel std
Shekhawati swv
Shendu shl
Sherdukpen sdp
Sherpa xsr
Shina scl
Sholaga sle
Shom Peng sii
Shumcho scu
Sikkimese sip
Simte smt
Sindhi snd
Singpho sgp
Sirmauri srx
Sora srb
Sourashtra saz
Spiti Bhoti spt
Stod Bhoti sbu
Sunam ssk
Surgujia sgj
Surjapuri sjp
Sylheti syl
Tagin tgj
Tamang, Eastern taj
Tamil tam
Telugu tel
Teressa tef
Thachanadan thn
Thangmi thf
Tharu, Chitwania the
Tharu, Dangaura thl
Tharu, Kathariya tkt
Tharu, Kochila thq
Tharu, Rana thr
Thulung tdh
Tibetan bod
Tinani lbf
Tiwa lax
Toda tcx
Toto txo
Tshangla tsj
Tulu tcy
Turi trd
Turung try
Ullatan ull
Urali url
Urdu urd
Uyghur uig
Vaagri Booli vaa
Vaiphei vap
Varhadi-Nagpuri vah
Varli vav
Vasavi vas
Vishavan vis
Waddar wbq
Wagdi wbr
Walungge ola
War-Jaintia aml
West Bengal Sign Language wbs
Yakkha ybh
Yerukula yeu
Zakhring zkr
Zangskari zau
Zou zom
l.browse_country()
 DZ
 AO
 BJ
 BW
 BF
 BI
 CM
 CV
 CF
 TD
 KM
 CG
 CI
 CD
 DJ
 EG
 GQ
 ER
 SZ
 ET
 GA
 GM
 GH
 GN
 GW
 KE
 LS
 LR
 LY
 MG
 MW
 ML
 MR
 MU
 YT
 MA
 MZ
 NA
 NE
 NG
 RE
 RW
 SH
 ST
 SN
 SC
 SL
 SO
 ZA
 SS
 SD
 TZ
 TG
 TN
 UG
 EH
 ZM
 ZW
 AI
 AG
 AR
 AW
 BS
 BB
 BZ
 BM
 BO
 BR
 VG
 CA
 BQ
 KY
 CL
 CO
 CR
 CU
 CW
 DM
 DO
 EC
 SV
 FK
 GF
 GL
 GD
 GP
 GT
 GY
 HT
 HN
 JM
 MQ
 MX
 MS
 NI
 PA
 PY
 PE
 PR
 BL
 KN
 LC
 MF
 PM
 VC
 SX
 SR
 TT
 TC
 VI
 US
 UY
 VE
 AF
 AM
 AZ
 BH
 BD
 BT
 IO
 BN
 KH
 CN
 HK
 MO
 TW
 CY
 TL
 GE
 IN
 ID
 IR
 IQ
 IL
 JP
 JO
 KZ
 KW
 KG
 LA
 LB
 MY
 MV
 MN
 MM
 NP
 KP
 OM
 PK
 PS
 PH
 QA
 SA
 SG
 KR
 LK
 SY
 TJ
 TH
 TR
 TM
 AE
 UZ
 VN
 YE
 AX
 AL
 AD
 AT
 BY
 BE
 BA
 BG
 HR
 CZ
 DK
 EE
 FO
 FI
 FR
 DE
 GI
 GR
 GG
 HU
 IS
 IE
 IM
 IT
 JE
 LV
 LI
 LT
 LU
 MT
 MD
 MC
 ME
 NL
 MK
 NO
 PL
 PT
 RO
 RU
 SM
 RS
 SK
 SI
 ES
 SE
 CH
 UA
 GB
 VA
 AS
 AU
 CX
 CC
 CK
 FJ
 PF
 GU
 KI
 MH
 FM
 NR
 NC
 NZ
 NU
 NF
 MP
 PW
 PG
 PN
 WS
 SB
 TK
 TO
 TV
 VU
 WF
 BI
 KM
 DJ
 ER
 ET
 KE
 MG
 MW
 MU
 YT
 MZ
 RE
 RW
 SC
 SO
 SS
 TZ
 UG
 ZM
 ZW
 AO
 CM
 CF
 TD
 CG
 CD
 GQ
 GA
 ST
 DZ
 EG
 LY
 MA
 SD
 TN
 EH
 BW
 SZ
 LS
 NA
 ZA
 BJ
 BF
 CV
 CI
 GM
 GH
 GN
 GW
 LR
 ML
 MR
 NE
 NG
 SH
 SN
 SL
 TG
 BZ
 CR
 SV
 GT
 HN
 MX
 NI
 PA
 AI
 AG
 AW
 BS
 BB
 VG
 BQ
 KY
 CU
 CW
 DM
 DO
 GD
 GP
 HT
 JM
 MQ
 MS
 PR
 BL
 KN
 LC
 MF
 VC
 SX
 TT
 TC
 VI
 BM
 CA
 GL
 PM
 US
 AR
 BO
 BR
 CL
 CO
 EC
 FK
 GF
 GY
 PY
 PE
 SR
 UY
 VE
 KZ
 KG
 TJ
 TM
 UZ
 CN
 HK
 MO
 TW
 JP
 MN
 KP
 KR
 AF
 BD
 BT
 IO
 IN
 IR
 MV
 NP
 PK
 LK
 BN
 KH
 TL
 ID
 LA
 MY
 MM
 PH
 SG
 TH
 VN
 AM
 AZ
 BH
 CY
 GE
 IQ
 IL
 JO
 KW
 LB
 OM
 PS
 QA
 SA
 SY
 TR
 AE
 YE
 BY
 BG
 CZ
 HU
 MD
 PL
 RO
 RU
 SK
 UA
 AX
 DK
 EE
 FO
 FI
 GG
 IS
 IE
 IM
 JE
 LV
 LT
 NO
 SE
 GB
 AL
 AD
 BA
 HR
 GI
 GR
 IT
 MT
 ME
 MK
 PT
 SM
 RS
 SI
 ES
 VA
 AT
 BE
 FR
 DE
 LI
 LU
 MC
 NL
 CH
 AU
 CX
 CC
 NZ
 NF
 FJ
 NC
 PG
 SB
 VU
 GU
 KI
 MH
 FM
 NR
 MP
 PW
 AS
 CK
 PF
 NU
 PN
 WS
 TK
 TO
 TV
 WF
