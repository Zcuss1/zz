import requests, threading, datetime, sys, os, time

def main():
	global auth, maxerr, api, pos, dely
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"Who's Eskey ?")
	print(f"Remake By Zcus")
	print(f"Crown & Trophy Duplicator.")
	print(f"")
	print(f"Kalau ngestuck tunggu aja")
	print(f"")
	api = "kitkabackend.eastus.cloudapp.azure.com:5010"
	auth = str(input("Auth Key: "))
	pos = int(input("""
0 = Round 1 (Eliminated)
1 = Round 2 (Eliminated)
2 = Round 3 (Eliminated)
3 = Round 3 (Winner)
Input: """))
	dely = float(input("\nDelay ( Ex. 0.5 | 1.0 | 2.0 and etc ): "))
	thr = int(input("\nThreads ( Default '1' | Jangan memasukan lebih dari 1 ): "))
	print("="*64)
	for _ in range(thr):
	        threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                negara = response.text.split('"Country":')[1].split(',')[0]
                                nama = response.text.split('"Username":')[1].split(',')[0]
                                trophy = response.text.split('"SkillRating":')[1].split(',')[0]
                                crown = response.text.split('"Crowns":')[1].split(',')[0]
                                print(f"\r[{dt.hour}:{dt.minute}:{dt.second}] {negara} | {nama} | {trophy} | {crown}")
                        elif response.status_code == 403 and response.text == "BANNED":
                                print(f"[{dt.hour}:{dt.minute}:{dt.second}] Account get Banned!")
                                break
                                sys.exit(0)
                        elif response.text == "SERVER_ERROR":
                                continue
                        else:
                                print(f"[{dt.hour}:{dt.minute}:{dt.second}] Error")
                                sys.stdout.flush()
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()
