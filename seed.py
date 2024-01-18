from app import db
from models import Sound, Word, List, WordSound, WordList

db.drop_all()
db.create_all()

db.session.commit()

bear = Sound(ipa_symbol="b", keyword="BEAR")
beaver = Sound(ipa_symbol="v", keyword="BEAVER")
blue = Sound(ipa_symbol="u", keyword="BLUE")
brown = Sound(ipa_symbol="aʊ", keyword="BROWN")
cat = Sound(ipa_symbol="k", keyword="CAT")
chicken = Sound(ipa_symbol="ʧ", keyword="CHICKEN")
coffee = Sound(ipa_symbol="ɑ", keyword="COFFEE")
dinosaur = Sound(ipa_symbol="n", keyword="DINOSAUR")
dog = Sound(ipa_symbol="d", keyword="DOG")
dust = Sound(ipa_symbol="ə", keyword="DUST")
feather = Sound(ipa_symbol="ð", keyword="FEATHER")
frog = Sound(ipa_symbol="f", keyword="FROG")
giraffe = Sound(ipa_symbol="ʤ", keyword="GIRAFFE")
goat = Sound(ipa_symbol="g", keyword="GOAT")
gold = Sound(ipa_symbol="oʊ", keyword="GOLD")
green = Sound(ipa_symbol="i", keyword="GREEN")
horse = Sound(ipa_symbol="h", keyword="HORSE")
jade = Sound(ipa_symbol="eɪ", keyword="JADE")
lime = Sound(ipa_symbol="aɪ", keyword="LIME")
lion = Sound(ipa_symbol="l", keyword="LION")
mauve = Sound(ipa_symbol="ɔ", keyword="MAUVE")
mouse = Sound(ipa_symbol="m", keyword="MOUSE")
panther = Sound(ipa_symbol="θ", keyword="PANTHER")
penguin = Sound(ipa_symbol="ŋ", keyword="PENGUIN")
pig = Sound(ipa_symbol="p", keyword="PIG")
pink = Sound(ipa_symbol="ɪ", keyword="PINK")
purple = Sound(ipa_symbol="ɜ", keyword="PURPLE")
rabbit = Sound(ipa_symbol="ɹ", keyword="RABBIT")
red = Sound(ipa_symbol="ɛ", keyword="RED")
sand = Sound(ipa_symbol="æ", keyword="SAND")
sheep = Sound(ipa_symbol="ʃ", keyword="SHEEP")
snake = Sound(ipa_symbol="s", keyword="SNAKE")
television = Sound(ipa_symbol="ʒ", keyword="TELEVISION")
turquoise = Sound(ipa_symbol="ɔɪ", keyword="TURQUOISE")
turtle = Sound(ipa_symbol="t", keyword="TURTLE")
wolf = Sound(ipa_symbol="w", keyword="WOLF")
wood = Sound(ipa_symbol="ʊ", keyword="WOOD")
yak = Sound(ipa_symbol="j", keyword="YAK")
zebra = Sound(ipa_symbol="z", keyword="ZEBRA")
extra = Sound(ipa_symbol="ɨ", keyword="GREEN") # same as i
extra2 = Sound(ipa_symbol="ʌ", keyword="DUST") # same as ə
extra3 = Sound(ipa_symbol="o", keyword="GOLD") # same as oʊ
extra4 = Sound(ipa_symbol="ɾ", keyword="DOG") # same as d
extra5 = Sound(ipa_symbol="ɯ", keyword="WOOD") # same as ʊ

db.session.add(bear)
db.session.add(beaver)
db.session.add(blue)
db.session.add(brown)
db.session.add(cat)
db.session.add(chicken)
db.session.add(coffee)
db.session.add(dinosaur)
db.session.add(dog)
db.session.add(dust)
db.session.add(feather)
db.session.add(frog)
db.session.add(giraffe)
db.session.add(goat)
db.session.add(gold)
db.session.add(green)
db.session.add(horse)
db.session.add(jade)
db.session.add(lime)
db.session.add(lion)
db.session.add(mauve)
db.session.add(mouse)
db.session.add(panther)
db.session.add(penguin)
db.session.add(pig)
db.session.add(pink)
db.session.add(purple)
db.session.add(rabbit)
db.session.add(red)
db.session.add(sand)
db.session.add(sheep)
db.session.add(snake)
db.session.add(television)
db.session.add(turquoise)
db.session.add(turtle)
db.session.add(wolf)
db.session.add(wood)
db.session.add(yak)
db.session.add(zebra)
db.session.add(extra)
db.session.add(extra2)
db.session.add(extra3)
db.session.add(extra4)
db.session.add(extra5)

db.session.commit()

wbear = Word(word="bear")
wbeaver = Word(word="beaver")
wblue = Word(word="blue")
wbrown = Word(word="brown")
wcat = Word(word="cat")
wchicken = Word(word="chicken")
wcoffee = Word(word="coffee")
wdinosaur = Word(word="dinosaur")
wdog = Word(word="dog")
wdust = Word(word="dust")
wfeather = Word(word="feather")
wfrog = Word(word="frog")
wgiraffe = Word(word="giraffe")
wgoat = Word(word="goat")
wgold = Word(word="gold")
wgreen = Word(word="green")
whorse = Word(word="horse")
wjade = Word(word="jade")
wlime = Word(word="lime")
wlion = Word(word="lion")
wmauve = Word(word="mauve")
wmouse = Word(word="mouse")
wpanther = Word(word="panther")
wpenguin = Word(word="penguin")
wpig = Word(word="pig")
wpink = Word(word="pink")
wpurple = Word(word="purple")
wrabbit = Word(word="rabbit")
wred = Word(word="red")
wsand = Word(word="sand")
wsheep = Word(word="sheep")
wsnake = Word(word="snake")
wtelevision = Word(word="television")
wturquoise = Word(word="turquoise")
wturtle = Word(word="turle")
wwolf = Word(word="wolf")
wwood = Word(word="wood")
wyak = Word(word="yak")
wzebra = Word(word="zebra")

db.session.add(wbear)
db.session.add(wbeaver)
db.session.add(wblue)
db.session.add(wbrown)
db.session.add(wcat)
db.session.add(wchicken)
db.session.add(wcoffee)
db.session.add(wdinosaur)
db.session.add(wdog)
db.session.add(wdust)
db.session.add(wfeather)
db.session.add(wfrog)
db.session.add(wgiraffe)
db.session.add(wgoat)
db.session.add(wgold)
db.session.add(wgreen)
db.session.add(whorse)
db.session.add(wjade)
db.session.add(wlime)
db.session.add(wlion)
db.session.add(wmauve)
db.session.add(wmouse)
db.session.add(wpanther)
db.session.add(wpenguin)
db.session.add(wpig)
db.session.add(wpink)
db.session.add(wpurple)
db.session.add(wrabbit)
db.session.add(wred)
db.session.add(wsand)
db.session.add(wsheep)
db.session.add(wsnake)
db.session.add(wtelevision)
db.session.add(wturquoise)
db.session.add(wturtle)
db.session.add(wwolf)
db.session.add(wwood)
db.session.add(wyak)
db.session.add(wzebra)

db.session.commit()

vowels = List(list_name="vowels", difficulty=1)
consonants = List(list_name="consonants", difficulty=2)

db.session.add(vowels)
db.session.add(consonants)

db.session.commit()

vowels.words.append(wblue)
vowels.words.append(wbrown)
vowels.words.append(wcoffee)
vowels.words.append(wdust)
vowels.words.append(wgold)
vowels.words.append(wgreen)
vowels.words.append(wjade)
vowels.words.append(wlime)
vowels.words.append(wmauve)
vowels.words.append(wpink)
vowels.words.append(wpurple)
vowels.words.append(wred)
vowels.words.append(wsand)
vowels.words.append(wturquoise)
vowels.words.append(wwood)

consonants.words.append(wbear)
consonants.words.append(wbeaver)
consonants.words.append(wcat)
consonants.words.append(wchicken)
consonants.words.append(wdinosaur)
consonants.words.append(wdog)
consonants.words.append(wfeather)
consonants.words.append(wfrog)
consonants.words.append(wgiraffe)
consonants.words.append(wgoat)
consonants.words.append(whorse)
consonants.words.append(wlion)
consonants.words.append(wmouse)
consonants.words.append(wpanther)
consonants.words.append(wpenguin)
consonants.words.append(wpig)
consonants.words.append(wrabbit)
consonants.words.append(wsheep)
consonants.words.append(wsnake)
consonants.words.append(wtelevision)
consonants.words.append(wturtle)
consonants.words.append(wwolf)
consonants.words.append(wyak)
consonants.words.append(wzebra)

db.session.commit()

a = WordSound(word_id = 1, sound_symbol="b", index=0)
b = WordSound(word_id = 1, sound_symbol="ɛ", index=1)
c = WordSound(word_id = 1, sound_symbol="ɹ", index=2)

d = WordSound(word_id = 2, sound_symbol="b", index=0)
e = WordSound(word_id = 2, sound_symbol="i", index=1)
f = WordSound(word_id = 2, sound_symbol="v", index=2)
g = WordSound(word_id = 2, sound_symbol="ɜ", index=3)

h = WordSound(word_id = 3, sound_symbol="b", index=0)
i = WordSound(word_id = 3, sound_symbol="l", index=1)
j = WordSound(word_id = 3, sound_symbol="u", index=2)

k = WordSound(word_id = 4, sound_symbol="b", index=0)
l = WordSound(word_id = 4, sound_symbol="ɹ", index=1)
m = WordSound(word_id = 4, sound_symbol="aʊ", index=2)
n = WordSound(word_id = 4, sound_symbol="n", index=3)

o = WordSound(word_id = 5, sound_symbol="k", index=0)
p = WordSound(word_id = 5, sound_symbol="æ", index=1)
q = WordSound(word_id = 5, sound_symbol="t", index=2)

r = WordSound(word_id = 6, sound_symbol="ʧ", index=0)
s = WordSound(word_id = 6, sound_symbol="ɪ", index=1)
t = WordSound(word_id = 6, sound_symbol="k", index=2)
u = WordSound(word_id = 6, sound_symbol="ɨ", index=3)
v = WordSound(word_id = 6, sound_symbol="n", index=4)

w = WordSound(word_id = 7, sound_symbol="k", index=0)
x = WordSound(word_id = 7, sound_symbol="ɑ", index=1)
y = WordSound(word_id = 7, sound_symbol="f", index=2)
z = WordSound(word_id = 7, sound_symbol="i", index=3)

aa = WordSound(word_id = 8, sound_symbol="d", index=0)
ab = WordSound(word_id = 8, sound_symbol="aɪ", index=1)
ac = WordSound(word_id = 8, sound_symbol="n", index=2)
ad = WordSound(word_id = 8, sound_symbol="ə", index=3)
ae = WordSound(word_id = 8, sound_symbol="s", index=4)
af = WordSound(word_id = 8, sound_symbol="ɔ", index=5)
ag = WordSound(word_id = 8, sound_symbol="ɹ", index=6)

ah = WordSound(word_id = 9, sound_symbol="d", index=0)
ai = WordSound(word_id = 9, sound_symbol="ɔ", index=1)
aj = WordSound(word_id = 9, sound_symbol="g", index=2)

ak = WordSound(word_id = 10, sound_symbol="d", index=0)
al = WordSound(word_id = 10, sound_symbol="ʌ", index=1)
am = WordSound(word_id = 10, sound_symbol="s", index=2)
an = WordSound(word_id = 10, sound_symbol="t", index=3)

ao = WordSound(word_id = 11, sound_symbol="f", index=0)
ap = WordSound(word_id = 11, sound_symbol="ɛ", index=1)
aq = WordSound(word_id = 11, sound_symbol="ð", index=2)
ar = WordSound(word_id = 11, sound_symbol="ɜ", index=3)

at = WordSound(word_id = 12, sound_symbol="f", index=0)
au = WordSound(word_id = 12, sound_symbol="ɹ", index=1)
av = WordSound(word_id = 12, sound_symbol="ɔ", index=2)
aw = WordSound(word_id = 12, sound_symbol="g", index=3)

ax = WordSound(word_id = 13, sound_symbol="ʤ", index=0)
ay = WordSound(word_id = 13, sound_symbol="ə", index=1)
az = WordSound(word_id = 13, sound_symbol="ɹ", index=2)
ba = WordSound(word_id = 13, sound_symbol="æ", index=3)
bb = WordSound(word_id = 13, sound_symbol="f", index=4)

bc = WordSound(word_id = 14, sound_symbol="g", index=0)
bd = WordSound(word_id = 14, sound_symbol="o", index=1)
be = WordSound(word_id = 14, sound_symbol="t", index=2)

bf = WordSound(word_id = 15, sound_symbol="g", index=0)
bg = WordSound(word_id = 15, sound_symbol="o", index=1)
bh = WordSound(word_id = 15, sound_symbol="l", index=2)
bi = WordSound(word_id = 15, sound_symbol="d", index=3)

bj = WordSound(word_id = 16, sound_symbol="g", index=0)
bk = WordSound(word_id = 16, sound_symbol="ɹ", index=1)
bl = WordSound(word_id = 16, sound_symbol="i", index=2)
bm = WordSound(word_id = 16, sound_symbol="n", index=3)

bn = WordSound(word_id = 17, sound_symbol="h", index=0)
bo = WordSound(word_id = 17, sound_symbol="ɔ", index=1)
bp = WordSound(word_id = 17, sound_symbol="ɹ", index=2)
bq = WordSound(word_id = 17, sound_symbol="s", index=3)

br = WordSound(word_id = 18, sound_symbol="ʤ", index=0)
bs = WordSound(word_id = 18, sound_symbol="eɪ", index=1)
bt = WordSound(word_id = 18, sound_symbol="d", index=2)

bv = WordSound(word_id = 19, sound_symbol="l", index=0)
bw = WordSound(word_id = 19, sound_symbol="aɪ", index=1)
bx = WordSound(word_id = 19, sound_symbol="m", index=2)

bz = WordSound(word_id = 20, sound_symbol="l", index=0)
ca = WordSound(word_id = 20, sound_symbol="aɪ", index=1)
cb = WordSound(word_id = 20, sound_symbol="ɨ", index=2)
cc = WordSound(word_id = 20, sound_symbol="n", index=3)

cd = WordSound(word_id = 21, sound_symbol="m", index=0)
ce = WordSound(word_id = 21, sound_symbol="ɔ", index=1)
cf = WordSound(word_id = 21, sound_symbol="v", index=2)

cg = WordSound(word_id = 22, sound_symbol="m", index=0)
ch = WordSound(word_id = 22, sound_symbol="aʊ", index=1)
ci = WordSound(word_id = 22, sound_symbol="s", index=2)

cj = WordSound(word_id = 23, sound_symbol="p", index=0)
ck = WordSound(word_id = 23, sound_symbol="æ", index=1)
cl = WordSound(word_id = 23, sound_symbol="n", index=2)
cm = WordSound(word_id = 23, sound_symbol="θ", index=3)
cn = WordSound(word_id = 23, sound_symbol="ɜ", index=4)

co = WordSound(word_id = 24, sound_symbol="p", index=0)
cp = WordSound(word_id = 24, sound_symbol="ɛ", index=1)
cq = WordSound(word_id = 24, sound_symbol="ŋ", index=2)
cr = WordSound(word_id = 24, sound_symbol="g", index=3)
cs = WordSound(word_id = 24, sound_symbol="w", index=4)
ct = WordSound(word_id = 24, sound_symbol="ɨ", index=5)
cu = WordSound(word_id = 24, sound_symbol="n", index=6)

cv = WordSound(word_id = 25, sound_symbol="p", index=0)
cw = WordSound(word_id = 25, sound_symbol="ɪ", index=1)
cx = WordSound(word_id = 25, sound_symbol="g", index=2)

cy = WordSound(word_id = 26, sound_symbol="p", index=0)
cz = WordSound(word_id = 26, sound_symbol="ɪ", index=1)
da = WordSound(word_id = 26, sound_symbol="ŋ", index=2)
bu = WordSound(word_id = 26, sound_symbol="k", index=3)

dc = WordSound(word_id = 27, sound_symbol="p", index=0)
dd = WordSound(word_id = 27, sound_symbol="ɜ", index=1)
de = WordSound(word_id = 27, sound_symbol="p", index=2)
df = WordSound(word_id = 27, sound_symbol="ə", index=3)
dg = WordSound(word_id = 27, sound_symbol="l", index=4)

dh = WordSound(word_id = 28, sound_symbol="ɹ", index=0)
di = WordSound(word_id = 28, sound_symbol="æ", index=1)
dj = WordSound(word_id = 28, sound_symbol="b", index=2)
dk = WordSound(word_id = 28, sound_symbol="ɨ", index=3)
dl = WordSound(word_id = 28, sound_symbol="t", index=4)

dm = WordSound(word_id = 29, sound_symbol="ɹ", index=0)
dn = WordSound(word_id = 29, sound_symbol="ɛ", index=1)
do = WordSound(word_id = 29, sound_symbol="d", index=2)

dp = WordSound(word_id = 30, sound_symbol="s", index=0)
dq = WordSound(word_id = 30, sound_symbol="æ", index=1)
dr = WordSound(word_id = 30, sound_symbol="n", index=2)
ds = WordSound(word_id = 30, sound_symbol="d", index=3)

dt = WordSound(word_id = 31, sound_symbol="ʃ", index=0)
du = WordSound(word_id = 31, sound_symbol="i", index=1)
dv = WordSound(word_id = 31, sound_symbol="p", index=2)

dw = WordSound(word_id = 32, sound_symbol="s", index=0)
dx = WordSound(word_id = 32, sound_symbol="n", index=1)
dy = WordSound(word_id = 32, sound_symbol="eɪ", index=2)
dz = WordSound(word_id = 32, sound_symbol="k", index=3)

ea = WordSound(word_id = 33, sound_symbol="t", index=0)
eb = WordSound(word_id = 33, sound_symbol="ɛ", index=1)
ec = WordSound(word_id = 33, sound_symbol="l", index=2)
ed = WordSound(word_id = 33, sound_symbol="ɨ", index=3)
ee = WordSound(word_id = 33, sound_symbol="v", index=4)
ef = WordSound(word_id = 33, sound_symbol="ɪ", index=5)
eg = WordSound(word_id = 33, sound_symbol="ʒ", index=6)
eh = WordSound(word_id = 33, sound_symbol="ə", index=7)
ei = WordSound(word_id = 33, sound_symbol="n", index=8)

ej = WordSound(word_id = 34, sound_symbol="t", index=0)
ek = WordSound(word_id = 34, sound_symbol="ɜ", index=1)
el = WordSound(word_id = 34, sound_symbol="k", index=2)
em = WordSound(word_id = 34, sound_symbol="ɔɪ", index=3)
en = WordSound(word_id = 34, sound_symbol="z", index=4)

eo = WordSound(word_id = 35, sound_symbol="t", index=0)
ep = WordSound(word_id = 35, sound_symbol="ɜ", index=1)
eq = WordSound(word_id = 35, sound_symbol="ɾ", index=2)
er = WordSound(word_id = 35, sound_symbol="ə", index=3)
es = WordSound(word_id = 35, sound_symbol="l", index=4)

et = WordSound(word_id = 36, sound_symbol="w", index=0)
eu = WordSound(word_id = 36, sound_symbol="ɯ", index=1)
ev = WordSound(word_id = 36, sound_symbol="l", index=2)
ew = WordSound(word_id = 36, sound_symbol="f", index=3)

ex = WordSound(word_id = 37, sound_symbol="w", index=0)
ey = WordSound(word_id = 37, sound_symbol="ɯ", index=1)
ez = WordSound(word_id = 37, sound_symbol="d", index=2)

fa = WordSound(word_id = 38, sound_symbol="j", index=0)
fb = WordSound(word_id = 38, sound_symbol="æ", index=1)
fc = WordSound(word_id = 38, sound_symbol="k", index=2)

fd = WordSound(word_id = 39, sound_symbol="z", index=0)
fe = WordSound(word_id = 39, sound_symbol="i", index=1)
ff = WordSound(word_id = 39, sound_symbol="b", index=2)
fg = WordSound(word_id = 39, sound_symbol="ɹ", index=3)
fh = WordSound(word_id = 39, sound_symbol="ə", index=4)

db.session.add(a)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)
db.session.add(f)
db.session.add(g)
db.session.add(h)
db.session.add(i)
db.session.add(j)
db.session.add(k)
db.session.add(l)
db.session.add(m)
db.session.add(n)
db.session.add(o)
db.session.add(p)
db.session.add(q)
db.session.add(r)
db.session.add(s)
db.session.add(t)
db.session.add(u)
db.session.add(v)
db.session.add(w)
db.session.add(x)
db.session.add(y)
db.session.add(z)
db.session.add(aa)
db.session.add(ab)
db.session.add(ac)
db.session.add(ad)
db.session.add(ae)
db.session.add(af)
db.session.add(ag)
db.session.add(ah)
db.session.add(ai)
db.session.add(aj)
db.session.add(ak)
db.session.add(al)
db.session.add(am)
db.session.add(an)
db.session.add(ao)
db.session.add(ap)
db.session.add(aq)
db.session.add(ar)
db.session.add(at)
db.session.add(au)
db.session.add(av)
db.session.add(aw)
db.session.add(ax)
db.session.add(ay)
db.session.add(az)
db.session.add(ba)
db.session.add(bb)
db.session.add(bc)
db.session.add(bd)
db.session.add(be)
db.session.add(bf)
db.session.add(bg)
db.session.add(bh)
db.session.add(bi)
db.session.add(bj)
db.session.add(bk)
db.session.add(bl)
db.session.add(bm)
db.session.add(bn)
db.session.add(bo)
db.session.add(bp)
db.session.add(bq)
db.session.add(br)
db.session.add(bs)
db.session.add(bt)
db.session.add(bv)
db.session.add(bw)
db.session.add(bx)
db.session.add(bz)
db.session.add(ca)
db.session.add(cb)
db.session.add(cc)
db.session.add(cd)
db.session.add(ce)
db.session.add(cf)
db.session.add(cg)
db.session.add(ch)
db.session.add(ci)
db.session.add(cj)
db.session.add(ck)
db.session.add(cl)
db.session.add(cm)
db.session.add(cn)
db.session.add(co)
db.session.add(cp)
db.session.add(cq)
db.session.add(cr)
db.session.add(cs)
db.session.add(ct)
db.session.add(cu)
db.session.add(cv)
db.session.add(cw)
db.session.add(cx)
db.session.add(cy)
db.session.add(cz)
db.session.add(da)
db.session.add(bu)
db.session.add(dc)
db.session.add(dd)
db.session.add(de)
db.session.add(df)
db.session.add(dg)
db.session.add(dh)
db.session.add(di)
db.session.add(dj)
db.session.add(dk)
db.session.add(dl)
db.session.add(dm)
db.session.add(dn)
db.session.add(do)
db.session.add(dp)
db.session.add(dq)
db.session.add(dr)
db.session.add(ds)
db.session.add(dt)
db.session.add(du)
db.session.add(dv)
db.session.add(dw)
db.session.add(dx)
db.session.add(dy)
db.session.add(dz)
db.session.add(ea)
db.session.add(eb)
db.session.add(ec)
db.session.add(ed)
db.session.add(ee)
db.session.add(ef)
db.session.add(eg)
db.session.add(eh)
db.session.add(ei)
db.session.add(ej)
db.session.add(ek)
db.session.add(el)
db.session.add(em)
db.session.add(en)
db.session.add(eo)
db.session.add(ep)
db.session.add(eq)
db.session.add(er)
db.session.add(es)
db.session.add(et)
db.session.add(eu)
db.session.add(ev)
db.session.add(ew)
db.session.add(ex)
db.session.add(ey)
db.session.add(ez)
db.session.add(fa)
db.session.add(fb)
db.session.add(fc)
db.session.add(fd)
db.session.add(fe)
db.session.add(ff)
db.session.add(fg)
db.session.add(fh)

db.session.commit()