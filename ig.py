# importing module 
from selenium import webdriver 
import os 
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager 

driver = webdriver.Chrome(ChromeDriverManager().install()) 

# enter receiver user name 
user = [['neatpreps'], ['reneil_da_writer'], ['chantaewilsonxd'], ['jamie.r.green'], ['allentroy74'], ['taneisethompson'], ['thecooliebabuja'], ['thewombofish'], ['neisha.law'], ['__danayyy'], ['ry_dan'], ['kimwebbja'], ['_serfiniti_'], ['affinityds_'], ['alyssa.chalayne_designs'], ['rav_bebii'], ['_jamizzle'], ['amzzcx'], ['_vxixc'], ['tedib_wp'], ['coreylg_yv'], ['delivereazze'], ['coucoutoiienftt'], ['zayn____._'], ['marshae_876'], ['king_ozzie'], ['yohann_townsend'], ['cameliagayle_'], ['bryannabaldie'], ['chadzamore'], ['jpounall_14'], ['daniecejarrett'], ['c.b.c__'], ['shaniiqueee'], ['matthewhutchinson_'], ['jamaicanhomehunter'], ['jori.lawson'], ['monie_untouchable'], ['roshellepinnock'], ['youngkahlifagrey'], ['_popsickle'], ['mynamescatface'], ['ant_tha_aviatrix'], ['ttg_ambitious1.0'], ['scarlet.shadow_'], ['dreaming_blackgirl.ja'], ['_happiitalie'], ['__smash__7'], ['su1_hoo'], ['raynorking'], ['cleveland.tomlinson'], ['steths_man'], ['deztacular'], ['i_van_persie'], ['quirky_christlydd'], ['dan.nielle_'], ['iamt_royal'], ['polo_sean_'], ['shvbbarxnkz'], ['khvlxd_11'], ['tiri876'], ['melanin_xx__'], ['geoallure'], ['d_antoinette_'], ['pierre.henry'], ['griffithstransporterservice'], ['jheanna_'], ['mvrk_96'], ['katiebearr17'], ['bernardlerie'], ['imjagofr'], ['laakan'], ['queenb_livia'], ['halieinthehouse'], ['w.tonilee'], ['leroythompson876'], ['jenoyrounz'], ['hindustani_d'], ['shakeilswaby'], ['cipher_x13'], ['bvri__'], ['chadlee96'], ['teddale_simpson'], ['cupid_heartzz'], ['chanchan_og'], ['nor.wyn'], ['dee.gills'], ['dez_jay_101'], ['arjuncp007'], ['876_user'], ['taintedgypsysoul'], ['skayhigh_'], ['zoeayanna'], ['king_odomz'], ['cunihaa'], ['madindian_4718'], ['adri_ande'], ['miguelnaveen1'], ['jamaicafoote'], ['tuwanie_'], ['pricelessqueen_nae_nae'], ['_delano_dlt'], ['gentles.oul'], ['jayswag2brite'], ['sarayoussef01'], ['byrianbailey8'], ['kidditofficial'], ['bookal_ladyshan'], ['kemical_7'], ['jeemz_d_individual'], ['steppa_run_road'], ['elle.s.t.lewis'], ['tjtheleo15'], ['noneotherthan.j'], ['blarsu'], ['jordiking1'], ['gavin_.white'], ['xo_ariya_xo'], ['ccobrian'], ['leafus_dova'], ['zowii__'], ['sanjae.x'], ['trendy_ster'], ['robertldstephenson'], ['sing_like_javid'], ['abi_noel01'], ['josephblackett'], ['deig_xo'], ['_kai_la'], ['dim__plez'], ['p.a.t.t.e.r.son'], ['_rai.n'], ['audacious_.tv'], ['oswin.wilson'], ['_donaldjr'], ['thee_wright_1'], ['ren_renzy'], ['brit_brat_mo'], ['mikhail.grant'], ['audacious_aidan'], ['crookedsmile_kai'], ['amberj8_'], ['bradleyluvarii'], ['raejon_powell'], ['boba.milkthy'], ['areanna_j'], ['keys2studentsuccess'], ['stephen_sid_james'], ['karli_black_'], ['iselaizzyy'], ['prince_kahail'], ['natasiafletcher'], ['mobayca'], ['desireedawsonmusic'], ['dpa_yaa'], ['shawnagowie'], ['robzla_vie'], ['omroy_a_smith'], ['where_is_toyan'], ['amandabent_'], ['kemi_kerr'], ['rad_spark'], ['shavanese_royalty'], ['janieverussell_'], ['rhoomzy'], ['aero_penha'], ['russell_don'], ['hblingboy'], ['millennial_foods'], ['__champagne.mami_'], ['slice_rj'], ['del_capri'], ['annabandulu'], ['gui_badda_boom'], ['bigbaddaboomsound'], ['mikalagarnet'], ['royleigh_w'], ['rassy_babe'], ['xo.peachy'], ['lizzie_morg876'], ['ebbie.j'], ['tellytakes'], ['jamling.sherpa'], ['jahnuary'], ['shanntelnicole'], ['whowillsaveyou'], ['ohhshatter'], ['mitchi_don'], ['x_denzil'], ['proud_dog_dad'], ['__sammymac'], ['jermaineahenry'], ['db_ui'], ['nonshalance'], ['wiz_ezel'], ['s.bernard94'], ['marlandownie'], ['patrickpinnockjr'], ['xo_khae'], ['nametoodeeptheysaid'], ['jojo_roqz'], ['annajustine11'], ['ianaolivia'], ['brina_noble'], ['__5ft.5'], ['alli_allsmiles'], ['henryblair.ar'], ['_nekie.sp'], ['melliererrie'], ['__firstedition__'], ['chavel_ann'], ['huntnick11'], ['krissannhaughton'], ['asheka93'], ['classychiqq_kris_may25'], ['yulanah.mullings'], ['tijuanaskky'], ['qxeentresh'], ['thatnormalchick'], ['aronemull'], ['karl_live'], ['blue_diamond_in_the_sun'], ['jord._.anne'], ['saamnicolex_'], ['multidimensionalwanderlust'], ['_.she.is.victoria._'], ['hon_collin'], ['mista_shyguy'], ['medleeeey'], ['____.lee.____'], ['kimikovs'], ['halftonechronicles'], ['joliegissy'], ['velisamonique'], ['amor_romi'], ['dennisjrcrooks'], ['___sam.i.am'], ['jovan_bullock'], ['____honeyy.kayy'], ['annya.romae'], ['lifeofmaniii'], ['indee._._'], ['daniinoey'], ['jil_danielle'], ['tinyy_sunshine'], ['the_real_mc_97'], ['_cee.jayy__'], ['shellianmorrison'], ['stxrdust777'], ['supreme_digital_production'], ['saxy_sarah23'], ['brookeab_'], ['thekeaneeye'], ['j.bbgxoxo'], ['janelleboos'], ['jevonjhenry'], ['razz.royalty'], ['karonmoni'], ['chambersshavel'], ['tanx7'], ['janea._'], ['_itsteddyy'], ['_ladyhall'], ['poole.hazel'], ['chef_wizzard'], ['chrisgrant_official'], ['b_boutique_cosmetics'], ['jamwinks'], ['piervs_'], ['mon_lifepurple'], ['shackeriaj'], ['jay_craaze'], ['jomorhys'], ['_webbaz'], ['chad_hayle'], ['kadblk9'], ['allisapollo'], ['geraldaarons'], ['heiskyleantonio'], ['samuelssabrina'], ['gabrielajmorris'], ['mario_downer'], ['fl_flanders'], ['jadeshalane'], ['torzz___'], ['b10fah'], ['demoykerrja'], ['alii_bedope'], ['raffiquemuir'], ['uv_found_juds'], ['miirahmajestic'], ['clove_star'], ['_chevzzz'], ['sadeekanthony'], ['castillo_leon_ce'], ['jia_876'], ['nevon.moore'], ['flora_dora_luv'], ['_ath.boyd'], ['finee.apple_'], ['ghaffarellis'], ['danielhenryofficiall'], ['tesiboo'], ['johnell.chambers'], ['_xoshimmz'], ['samiilala_snooks'], ['san_tana______'], ['clavii21'], ['radomedz'], ['jahjah_rain'], ['clintond1st'], ['jg_platt'], ['gesta_ovo'], ['ajene_binns'], ['gk_the_trusted_advisor'], ['malikekellier'], ['ms_lia_love'], ['chrisanndouglas'], ['_teadan'], ['cinnaman_riq'], ['afrikali_bebek'], ['jodz.c'], ['getthereja'], ['nathanael_amore'], ['abbi_roseja'], ['rozzanne_'], ['ae_terry'], ['__king_treecy'], ['shyliizzle'], ['everton_reid'], ['mhrwill'], ['bonita_melia'], ['lili_felii'], ['ollieoasis'], ['upbeet_nutrition'], ['chanel_le.h'], ['jevon_k.reid'], ['king._.wembz'], ['pal2flow'], ['tareekdc'], ['livia_greatness'], ['sbuckeridge'], ['le_shawnag'], ['conradmathison'], ['tavharri'], ['alyssia_myrie'], ['e46ixmatt'], ['avaris_'], ['julianmckayjr'], ['_x.sun.shine'], ['njamair'], ['meghana.mcm'], ['n_morgans_photography'], ['omz_rx'], ['westechlimited'], ['tinaa_t.t'], ['strongone__'], ['sammm876'], ['relativelyshan'], ['britneyyy_______'], ['sherryxlove'], ['helium.sh'], ['coloured_eyes'], ['caleighsayshey'], ['lts.limited'], ['myersglenroy'], ['elle_essence'], ['kiteinflight'], ['louverture_hacker'], ['toastytoast98'], ['pierre.gordon'], ['sanja_jackson'], ['anrkiss'], ['longlegs_prettysmile'], ['xoxomomo_'], ['english_foreigners'], ['vvidal876'], ['nicksnyder.gif'], ['eus2popmoly'], ['kai_nikka'], ['lishana.lishana'], ['whitney.a.l'], ['sing_javid'], ['itsdaneille'], ['daveiamagnus'], ['digeneraldesign'], ['asha_queenie_muir'], ['ahkeel_'], ['asaniharrison'], ['kerron_art'], ['grantoflexx'], ['skoolboyja'], ['ambrose_williamsjr'], ['sanjaystephens'], ['the_donnel'], ['frescocam'], ['shanidropjaws'], ['fivegablesjamaica'], ['slick2small'], ['troy_vidallen'], ['flowazbwoi'], ['a_keela'], ['chentastic1']]
 
message_ = ("This message was sent to you by a software that automates direct messaging for Instagram, brought to you by your friendly neighborhood hacker.") 


class bot: 
	def __init__(self, username, password, user, message): 
		self.username = username 
		self.password = password 
		self.user = user 
		self.message = message 
		self.base_url = 'https://www.instagram.com/'
		self.bot = driver 
		self.login() 

	def login(self): 
		self.bot.get(self.base_url) 

		enter_username = WebDriverWait(self.bot, 20).until( 
			expected_conditions.presence_of_element_located((By.NAME, 'username'))) 
		enter_username.send_keys(self.username) 
		enter_password = WebDriverWait(self.bot, 20).until( 
			expected_conditions.presence_of_element_located((By.NAME, 'password'))) 
		enter_password.send_keys(self.password) 
		enter_password.send_keys(Keys.RETURN) 
		time.sleep(5) 

		# first pop-up 
		self.bot.find_element_by_xpath( 
			'//*[@id="react-root"]/section/main/div/div/div/div/button').click() 
		time.sleep(3) 

		# 2nd pop-up 
		self.bot.find_element_by_xpath( 
			'/html/body/div[4]/div/div/div/div[3]/button[2]').click() 
		time.sleep(4) 

		# direct button 
		self.bot.find_element_by_xpath( 
			'//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click() 
		time.sleep(6) 

		# clicks on pencil icon 
		self.bot.find_element_by_xpath( 
			'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click() 
		time.sleep(3) 
		for i in user: 

			# enter the username 
			self.bot.find_element_by_xpath( 
				'/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) 
			time.sleep(10) 

			# click on the username 
			self.bot.find_element_by_xpath( 
				'/html/body/div[5]/div/div/div[2]/div[2]/div/div').click() 
			time.sleep(10) 

			# next button 
			self.bot.find_element_by_xpath( 
				'/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click() 
			time.sleep(10) 

			# click on message area 
			send = self.bot.find_element_by_xpath( 
				'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') 

			# types message 
			send.send_keys(self.message) 
			time.sleep(3) 

			# send message 
			send.send_keys(Keys.RETURN) 
			time.sleep(3) 

			# clicks on direct option or pencl icon 
			self.bot.find_element_by_xpath( 
				'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
			time.sleep(2) 


def init(): 
	bot('username', 'password', user, message_) 

	# when our program ends it will show "done". 
	input("DONE") 


# calling the function 
init() 
