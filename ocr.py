import easyocr
import pyttsx3
from googletrans import Translator
translator=Translator()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()
reader = easyocr.Reader(['ta'])
#SUPPORTED LANGUAGES AND THEIR CODES
'''
1. Abaza = abq
2. Adyghe = ady
3. Afrikaans = af
4. Angika = ang
5. Arabic = ar
6. Assamese = as
7. Avar = ava
8. Azerbaijani = az
9. Belarusian = be
10. Bulgarian = bg
11. Bihari = bh
12. Bhojpuri = bho
13. Bengali = bn
14. Bosnian = bs
15. Simplified Chinese = ch_sim
16. Traditional Chinese = ch_tra
17. Chechen = che
18. Czech = cs
19. Welsh = cy
20. Danish = da
21. Dargwa = dar
22. German = de
23. English = en
24. Spanish = es
25. Estonian = et
26. Persian (Farsi) = fa
27. French = fr
28. Irish = ga
29. Goan Konkani = gom
30. Hindi = hi
31. Croatian= hr
32. Hungarian = hu
33. Indonesian= id
34. Ingush = inh
35. Icelandic = is
36. Italian = it
37. Japanese = ja
38. Kabardian = kbd
39. Kannada = kn
40. Korean = ko
41. Kurdish = ku
42. Latin = la
43. Lak = lbe
44. Lezghian = lez
45. Lithuanian= lt
46. Latvian = lv
47. Magahi = mah
48. Maithili = mai
49. Maori = mi
50. Mongolian= mn
51. Marathi = mr
52. Malay = ms
53. Maltese = mt
54. Nepali = ne
55. Newari = new
56. Dutch = nl
57. Norwegian= no
58. Occitan = oc
59. Pali = pi
60. Polish = pl
61. Portuguese= pt
62. Romanian = ro
63. Russian = ru
64. Serbian (cyrillic) = rs_cyrillic
65. Serbian (latin) = rs_latin
66. Nagpuri = sck
67. Slovak = sk
68. Slovenian = sl
69. Albanian = sq
70. Swedish = sv
71. Swahili = sw
72. Tamil = ta
73. Tabassarant= ab
74. Telugu = te
75. Thai = th
76. Tajik= tjk
77. Tagalog = tl
78. Turkish = tr
79. Uyghur = ug
80. Ukranian = uk
81. Urdu = ur
82. Uzbek = uz
83. Vietnamese = vi
'''
while True:
 filename = input("enter the file name: ")
 results = reader.readtext(filename)
 txt_op = ''
 for result in results:
    txt_op += result[1] + ' '
 print(txt_op)

output = txt_op
out = translator.translate(output, dest='en')
a = print("\t\tCONVERTED TEXT IS:\t\t\n ", out.text)
speak(a)
