# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:14:02 2016

@author: Jsn
"""

# import library untuk generate angka random
from random import randint, random

# import library untuk copy list
from copy import deepcopy

import Tkinter

root = Tkinter.Tk() # panggil GUI

# deklarasi variabel
output = Tkinter.StringVar()
inputan = []

### DAFTAR FUNGSI - START ###

def convert_ke_integer(array_char, array_int):
    for k in range (0, len(inputan)):
        if array_char[k] == "a":
            array_int[k] = 1
        elif array_char[k] == "b":
            array_int[k] = 2
        elif array_char[k] == "c":
            array_int[k] = 3
        elif array_char[k] == "d":
            array_int[k] = 4
        elif array_char[k] == "e":
            array_int[k] = 5
        elif array_char[k] == "f":
            array_int[k] = 6
        elif array_char[k] == "g":
            array_int[k] = 7
        elif array_char[k] == "h":
            array_int[k] = 8
        elif array_char[k] == "i":
            array_int[k] = 9
        elif array_char[k] == "j":
            array_int[k] = 10
        elif array_char[k] == "k":
            array_int[k] = 11
        elif array_char[k] == "l":
            array_int[k] = 12
        elif array_char[k] == "m":
            array_int[k] = 13
        elif array_char[k] == "n":
            array_int[k] = 14
        elif array_char[k] == "o":
            array_int[k] = 15
        elif array_char[k] == "p":
            array_int[k] = 16
        elif array_char[k] == "q":
            array_int[k] = 17
        elif array_char[k] == "r":
            array_int[k] = 18
        elif array_char[k] == "s":
            array_int[k] = 19
        elif array_char[k] == "t":
            array_int[k] = 20
        elif array_char[k] == "u":
            array_int[k] = 21
        elif array_char[k] == "v":
            array_int[k] = 22
        elif array_char[k] == "w":
            array_int[k] = 23
        elif array_char[k] == "x":
            array_int[k] = 24
        elif array_char[k] == "y":
            array_int[k] = 25
        elif array_char[k] == "z":
            array_int[k] = 26
        else:
            array_int[k] = 0
    return array_int
    
def convert_ke_char(array_char, array_int):
    for k in range (0, len(inputan)):
        if array_int[k] == 1:
            array_char[k] = "a"
        elif array_int[k] == 2:
            array_char[k] = "b"
        elif array_int[k] == 3:
            array_char[k] = "c"
        elif array_int[k] == 4:
            array_char[k] = "d"
        elif array_int[k] == 5:
            array_char[k] = "e"
        elif array_int[k] == 6:
            array_char[k] = "f"
        elif array_int[k] == 7:
            array_char[k] = "g"
        elif array_int[k] == 8:
            array_char[k] = "h"
        elif array_int[k] == 9:
            array_char[k] = "i"
        elif array_int[k] == 10:
            array_char[k] = "j"
        elif array_int[k] == 11:
            array_char[k] = "k"
        elif array_int[k] == 12:
            array_char[k] = "l"
        elif array_int[k] == 13:
            array_char[k] = "m"
        elif array_int[k] == 14:
            array_char[k] = "n"
        elif array_int[k] == 15:
            array_char[k] = "o"
        elif array_int[k] == 16:
            array_char[k] = "p"
        elif array_int[k] == 17:
            array_char[k] = "q"
        elif array_int[k] == 18:
            array_char[k] = "r"
        elif array_int[k] == 19:
            array_char[k] = "s"
        elif array_int[k] == 20:
            array_char[k] = "t"
        elif array_int[k] == 21:
            array_char[k] = "u"
        elif array_int[k] == 22:
            array_char[k] = "v"
        elif array_int[k] == 23:
            array_char[k] = "w"
        elif array_int[k] == 24:
            array_char[k] = "x"
        elif array_int[k] == 25:
            array_char[k] = "y"
        elif array_int[k] == 26:
            array_char[k] = "z"
        else:
            array_char[k] = "_"
    return array_char

def input_char():
    jml_char = int(E2.get())
    
    # kalau jumlah char di bawah 11 dan di atas 1 baru bisa jalan
    if jml_char < 11 and jml_char > 1:
        L3 = Tkinter.Label(frame, text = "Input char :")
        L3.place(y = 130, width = 200, height = 35)    
        
        posisi_char = 0
        
        # buat entry sebanyak jumlah char
        for i in range (0, jml_char)    :
            inputan.append(Tkinter.Entry(frame))
            inputan[i].place(x = 150 + posisi_char, y = 130, width = 20, height = 35)
            posisi_char = posisi_char + 30    
    
        # supaya tombol tidak bisa dipencet lagi
        E2.config(state='disabled')
        input_char.config(state='disabled')
    
        # buat button start generation    
        global start_btn # dibuat global agar bisa dipake lagi di function start_generate()
        start_btn = Tkinter.Button(frame, text = "start generation", command = start_generate)
        start_btn.place(y = 190, x = 150, width = 200, height = 35)    
        
        #output.set("%.2f" % jml_char)

def start_generate():
    isi_semua = True
    
    # cek apa semua sudah terisi
    for j in range (len(inputan)):
        if len(inputan[j].get()) != 1:
            isi_semua = False
        else:
            inputan[j].config(state='disabled')
    
    # kalau sudah terisi semua baru keluar text area
    if isi_semua == True:
        start_btn.config(state='disabled')
        textarea = Tkinter.Entry(frame, textvariable = output)
        textarea.place(x = 30, y = 250, width = 443, height = 200)    
        textarea.config(state='disabled')
                
        # deklarasi size array
        global array_inputan, array_solusi, array_krom1, array_krom2, array_krom3
        global array_krom4, array_krom5, array_krom6, array_krom7, array_krom8
        global array_krom9, array_krom10, char_krom1, char_krom2, char_krom3
        global char_krom4, char_krom5, char_krom6, char_krom7, char_krom8, char_krom9
        global char_krom10
        array_inputan = [0] * len(inputan)
        array_solusi = [0] * len(inputan)
        array_krom1 = [0] * len(inputan)
        array_krom2 = [0] * len(inputan)
        array_krom3 = [0] * len(inputan)
        array_krom4 = [0] * len(inputan)
        array_krom5 = [0] * len(inputan)
        array_krom6 = [0] * len(inputan)
        array_krom7 = [0] * len(inputan)
        array_krom8 = [0] * len(inputan)
        array_krom9 = [0] * len(inputan)
        array_krom10 = [0] * len(inputan)
        char_krom1 = [" "] * len(inputan)
        char_krom2 = [" "] * len(inputan)
        char_krom3 = [" "] * len(inputan)
        char_krom4 = [" "] * len(inputan)
        char_krom5 = [" "] * len(inputan)
        char_krom6 = [" "] * len(inputan)
        char_krom7 = [" "] * len(inputan)
        char_krom8 = [" "] * len(inputan)
        char_krom9 = [" "] * len(inputan)
        char_krom10 = [" "] * len(inputan)
        
        # buat output inputan user
        print "Inputan\t\t[", 
        for j in range (len(inputan)):    
            print inputan[j].get().lower(),
            array_inputan[j] = inputan[j].get().lower()
        print "]\n"
        
        #####    MULAI METODE ALGORITMA GENETIK    #####
        
        ### TAHAP 1. MEMBANGKITKAN POPULASI AWAL ###
        
        # jalanin fungsi yg mengubah huruf jadi angka
        array_solusi = convert_ke_integer(array_inputan, array_solusi)
        """
        print "Convert\t\t", array_solusi, "\n"
        """
        generasi = 1
        print "Generasi ke", generasi
        
        # randomize kromosom2 awal
        for l in range (len(inputan)):
            array_krom1[l] = randint(1, 26)
            array_krom2[l] = randint(1, 26)
            array_krom3[l] = randint(1, 26)
            array_krom4[l] = randint(1, 26)
            array_krom5[l] = randint(1, 26)
            array_krom6[l] = randint(1, 26)
            array_krom7[l] = randint(1, 26)
            array_krom8[l] = randint(1, 26)
            array_krom9[l] = randint(1, 26)
            array_krom10[l] = randint(1, 26)
        
        char_krom1 = convert_ke_char(char_krom1, array_krom1)
        char_krom2 = convert_ke_char(char_krom2, array_krom2)
        char_krom3 = convert_ke_char(char_krom3, array_krom3)
        char_krom4 = convert_ke_char(char_krom4, array_krom4)
        char_krom5 = convert_ke_char(char_krom5, array_krom5)
        char_krom6 = convert_ke_char(char_krom6, array_krom6)
        char_krom7 = convert_ke_char(char_krom7, array_krom7)
        char_krom8 = convert_ke_char(char_krom8, array_krom8)
        char_krom9 = convert_ke_char(char_krom9, array_krom9)
        char_krom10 = convert_ke_char(char_krom10, array_krom10)
        
        print "Kromosom1\t", char_krom1
        print "Kromosom2\t", char_krom2
        print "Kromosom3\t", char_krom3
        print "Kromosom4\t", char_krom4
        print "Kromosom5\t", char_krom5
        print "Kromosom6\t", char_krom6
        print "Kromosom7\t", char_krom7
        print "Kromosom8\t", char_krom8
        print "Kromosom9\t", char_krom9
        print "Kromosom10\t", char_krom10#, "\n"
        
        ### TAHAP 2. EVALUASI ###
        
        while (generasi < 10000):
            
            # deklarasi fungsi objektif
            global f_obj1, f_obj2, f_obj3, f_obj4, f_obj5, f_obj6
            global f_obj7, f_obj8, f_obj9, f_obj10, f_rata2

            f_obj1 = 0
            f_obj2 = 0
            f_obj3 = 0
            f_obj4 = 0
            f_obj5 = 0
            f_obj6 = 0
            f_obj7 = 0
            f_obj8 = 0
            f_obj9 = 0
            f_obj10 = 0
            
            # menghitung fungsi objektif
            f_obj1 = fungsi_objektif(array_krom1)
            f_obj2 = fungsi_objektif(array_krom2)
            f_obj3 = fungsi_objektif(array_krom3)
            f_obj4 = fungsi_objektif(array_krom4)
            f_obj5 = fungsi_objektif(array_krom5)
            f_obj6 = fungsi_objektif(array_krom6)
            f_obj7 = fungsi_objektif(array_krom7)
            f_obj8 = fungsi_objektif(array_krom8)
            f_obj9 = fungsi_objektif(array_krom9)
            f_obj10 = fungsi_objektif(array_krom10)
            f_rata2 = (f_obj1 + f_obj2 + f_obj3 + f_obj4 + f_obj5 + f_obj6 + f_obj7 + f_obj8 + f_obj9 + f_obj10) / 10
            """
            print "F_Objektif1:\t", f_obj1
            print "F_Objektif2:\t", f_obj2
            print "F_Objektif3:\t", f_obj3
            print "F_Objektif4:\t", f_obj4
            print "F_Objektif5:\t", f_obj5
            print "F_Objektif6:\t", f_obj6
            print "F_Objektif7:\t", f_obj7
            print "F_Objektif8:\t", f_obj8
            print "F_Objektif9:\t", f_obj9
            print "F_Objektif10:\t", f_obj10, "\n"
            """
            print "Fungsi Objektif Generasi", generasi, ":\t", f_rata2, "\n"
            
            # kalau sudah mencapai solusi, keluar dari loop
            if f_rata2 == 0:
                pesan = "Hasil ditemukan pada Generasi ke", generasi
                break
            elif generasi == 9999:
                pesan = "Hasil TIDAK ditemukan sampai generasi ke", generasi
            
            ### TAHAP 3. SELEKSI ###
            
            # menghitung fungsi fitness
            fitness1 = fungsi_fitness(f_obj1)
            fitness2 = fungsi_fitness(f_obj2)
            fitness3 = fungsi_fitness(f_obj3)
            fitness4 = fungsi_fitness(f_obj4)
            fitness5 = fungsi_fitness(f_obj5)
            fitness6 = fungsi_fitness(f_obj6)
            fitness7 = fungsi_fitness(f_obj7)
            fitness8 = fungsi_fitness(f_obj8)
            fitness9 = fungsi_fitness(f_obj9)
            fitness10 = fungsi_fitness(f_obj10)
            """
            print "Fitness1:\t", fitness1
            print "Fitness2:\t", fitness2
            print "Fitness3:\t", fitness3
            print "Fitness4:\t", fitness4
            print "Fitness5:\t", fitness5
            print "Fitness6:\t", fitness6
            print "Fitness7:\t", fitness7
            print "Fitness8:\t", fitness8
            print "Fitness9:\t", fitness9
            print "Fitness10:\t", fitness10, "\n"
            """
            # hitung total fitness
            total_fitness = fitness1 + fitness2 + fitness3 + fitness4 + fitness5 + fitness6 + fitness7 + fitness8 + fitness9 + fitness10
            
            # hitung probabilitas
            p1 = probabilitas(fitness1, total_fitness)
            p2 = probabilitas(fitness2, total_fitness)
            p3 = probabilitas(fitness3, total_fitness)
            p4 = probabilitas(fitness4, total_fitness)
            p5 = probabilitas(fitness5, total_fitness)
            p6 = probabilitas(fitness6, total_fitness)
            p7 = probabilitas(fitness7, total_fitness)
            p8 = probabilitas(fitness8, total_fitness)
            p9 = probabilitas(fitness9, total_fitness)
            p10 = probabilitas(fitness10, total_fitness)
            """
            print "Probabilitas1:\t", p1
            print "Probabilitas2:\t", p2
            print "Probabilitas3:\t", p3
            print "Probabilitas4:\t", p4
            print "Probabilitas5:\t", p5
            print "Probabilitas6:\t", p6
            print "Probabilitas7:\t", p7
            print "Probabilitas8:\t", p8
            print "Probabilitas9:\t", p9
            print "Probabilitas10:\t", p10, "\n"
            """
            # persiapin roulette wheel
            c1 = p1
            c2 = p1 + p2
            c3 = p1 + p2 + p3
            c4 = p1 + p2 + p3 + p4
            c5 = p1 + p2 + p3 + p4 + p5
            c6 = p1 + p2 + p3 + p4 + p5 + p6
            c7 = p1 + p2 + p3 + p4 + p5 + p6 + p7
            c8 = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
            c9 = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
            c10 = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
            """
            print "C1:\t", c1
            print "C2:\t", c2
            print "C3:\t", c3
            print "C4:\t", c4
            print "C5:\t", c5
            print "C6:\t", c6
            print "C7:\t", c7
            print "C8:\t", c8
            print "C9:\t", c9
            print "C10:\t", c10, "\n"
            """
            # lakukan roulette sebanyak populasi, populasinya cuma 3 kromosom
            pil1 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil2 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil3 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil4 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil5 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil6 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil7 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil8 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil9 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            pil10 = roulette_wheel(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
            """
            print "Hasil pemilihan Roulette wheel1:\t", pil1
            print "Hasil pemilihan Roulette wheel2:\t", pil2
            print "Hasil pemilihan Roulette wheel3:\t", pil3
            print "Hasil pemilihan Roulette wheel4:\t", pil4
            print "Hasil pemilihan Roulette wheel5:\t", pil5
            print "Hasil pemilihan Roulette wheel6:\t", pil6
            print "Hasil pemilihan Roulette wheel7:\t", pil7
            print "Hasil pemilihan Roulette wheel8:\t", pil8
            print "Hasil pemilihan Roulette wheel9:\t", pil9
            print "Hasil pemilihan Roulette wheel10:\t", pil10, "\n"
            """
            # buat cadangan kromosom
            temp_krom1 = array_krom1
            temp_krom2 = array_krom2
            temp_krom3 = array_krom3
            temp_krom4 = array_krom4
            temp_krom5 = array_krom5
            temp_krom6 = array_krom6
            temp_krom7 = array_krom7
            temp_krom8 = array_krom8
            temp_krom9 = array_krom9
            temp_krom10 = array_krom10
            
            # mendefinisikan kandidat kromosom baru yang lolos seleksi
            array_krom1 = rouletted_kromosom(pil1, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom2 = rouletted_kromosom(pil2, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom3 = rouletted_kromosom(pil3, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom4 = rouletted_kromosom(pil4, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom5 = rouletted_kromosom(pil5, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom6 = rouletted_kromosom(pil6, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom7 = rouletted_kromosom(pil7, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom8 = rouletted_kromosom(pil8, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom9 = rouletted_kromosom(pil9, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            array_krom10 = rouletted_kromosom(pil10, temp_krom1, temp_krom2, temp_krom3, temp_krom4, temp_krom5, temp_krom6, temp_krom7, temp_krom8, temp_krom9, temp_krom10)
            """
            print "Kromosom setelah seleksi1:\t", array_krom1
            print "Kromosom setelah seleksi2:\t", array_krom2
            print "Kromosom setelah seleksi3:\t", array_krom3
            print "Kromosom setelah seleksi4:\t", array_krom4
            print "Kromosom setelah seleksi5:\t", array_krom5
            print "Kromosom setelah seleksi6:\t", array_krom6
            print "Kromosom setelah seleksi7:\t", array_krom7
            print "Kromosom setelah seleksi8:\t", array_krom8
            print "Kromosom setelah seleksi9:\t", array_krom9
            print "Kromosom setelah seleksi10:\t", array_krom10, "\n"
            """
            ### TAHAP 4. CROSSOVER ###
            
            # set probabilitas crossover
            pc = 0.25 # 25%

            size_parent = []
            
            # bikin code dari pseudocode di slide
            k = 0
            while (k < 10):
                rk = random()
                """
                print "r", k, ":\t", rk
                """
                if (rk < pc):
                    size_parent.append(k+1)
                    """
                    print size_parent
                    """
                k = k + 1
            """
            print " "
            """
            array_offspring = [array_krom1, array_krom2, array_krom3, array_krom4, array_krom5, array_krom6, array_krom7, array_krom8, array_krom9, array_krom10]
            
            if (len(size_parent) > 1):
                
                for q in range (len(size_parent)):
                    # random angka 
                    angka_random = randint(0, len(size_parent)-1)
                    # angka akan di random ulang apabila sama dengan q. untuk menghindari kromosom crossover dengan kromosom yang sama
                    while (angka_random == q):
                        angka_random = randint(0, len(size_parent)-1)
                    """
                    print "q: ", q, " angka_random: ", angka_random, "\n"
                    """
                    array_offspring[q] = crossover(array_offspring[q], array_offspring[angka_random])                                    
            """
            print "\nOffspring1:\t\t", array_offspring[0]
            print "Offspring2:\t\t", array_offspring[1]
            print "Offspring3:\t\t", array_offspring[2]
            print "Offspring4:\t\t", array_offspring[3]
            print "Offspring5:\t\t", array_offspring[4]
            print "Offspring6:\t\t", array_offspring[5]
            print "Offspring7:\t\t", array_offspring[6]
            print "Offspring8:\t\t", array_offspring[7]
            print "Offspring9:\t\t", array_offspring[8]
            print "Offspring10:\t\t", array_offspring[9], "\n"
            """
                        
            ### TAHAP 5. MUTASI ###        
            # set probabilitas mutasi
            pm = 0.1 # 10%
            
            # hitung jumlah gen yang bermutasi
            # banyak mutasi = jml gen x jml kromosom * mutation rate
            banyaknya_mutasi = len(inputan) * 10 * pm 
            
            # dibulatkan
            banyaknya_mutasi = int(banyaknya_mutasi)
            """
            print "Banyaknya mutasi:\t", banyaknya_mutasi, "\n"
            """
            # set batasan
            batas1 = len(inputan)-1
            batas2 = (len(inputan)*2)-1
            batas3 = (len(inputan)*3)-1
            batas4 = (len(inputan)*4)-1
            batas5 = (len(inputan)*5)-1
            batas6 = (len(inputan)*6)-1
            batas7 = (len(inputan)*7)-1
            batas8 = (len(inputan)*8)-1
            batas9 = (len(inputan)*9)-1
            batas_akhir = (len(inputan) * 10) - 1
            
            # random posisi angka sebanyak jumlah mutasi
            mutasi = 0
            
            while mutasi < banyaknya_mutasi:
                
                # bikin random
                r = randint(0, batas_akhir)
                """
                print "Mutasi urutan ke:\t", r+1
                """
                # mutasi secara random
                if (r >= 0 and r <= batas1):
                    if array_offspring[0][r] != 0:
                        array_offspring[0][r] = randint(1, 26)
                elif (r > batas1 and r <= batas2):
                    if array_offspring[1][r%len(inputan)] != 0:
                        array_offspring[1][r%len(inputan)] = randint(1, 26)
                elif (r > batas2 and r <= batas3):
                    if array_offspring[2][r%len(inputan)] != 0:
                        array_offspring[2][r%len(inputan)] = randint(1, 26)
                elif (r > batas3 and r <= batas4):
                    if array_offspring[3][r%len(inputan)] != 0:
                        array_offspring[3][r%len(inputan)] = randint(1, 26)
                elif (r > batas4 and r <= batas5):
                    if array_offspring[4][r%len(inputan)] != 0:
                        array_offspring[4][r%len(inputan)] = randint(1, 26)
                elif (r > batas5 and r <= batas6):
                    if array_offspring[5][r%len(inputan)] != 0:
                        array_offspring[5][r%len(inputan)] = randint(1, 26)
                elif (r > batas6 and r <= batas7):
                    if array_offspring[6][r%len(inputan)] != 0:
                        array_offspring[6][r%len(inputan)] = randint(1, 26)
                elif (r > batas7 and r <= batas8):
                    if array_offspring[7][r%len(inputan)] != 0:
                        array_offspring[7][r%len(inputan)] = randint(1, 26)
                elif (r > batas8 and r <= batas9):
                    if array_offspring[8][r%len(inputan)] != 0:
                        array_offspring[8][r%len(inputan)] = randint(1, 26)
                else:
                    if array_offspring[9][r%len(inputan)] != 0:
                        array_offspring[9][r%len(inputan)] = randint(1, 26)
                """
                print "Offspring setelah mutasi"
                print "Offspring1:\t", array_offspring[0]
                print "Offspring2:\t", array_offspring[1]
                print "Offspring3:\t", array_offspring[2]
                print "Offspring4:\t", array_offspring[3]
                print "Offspring5:\t", array_offspring[4]
                print "Offspring6:\t", array_offspring[5]
                print "Offspring7:\t", array_offspring[6]
                print "Offspring8:\t", array_offspring[7]
                print "Offspring9:\t", array_offspring[8]
                print "Offspring10:\t", array_offspring[9], "\n"
                """
                mutasi = mutasi + 1
            
            # set offspring jadi kromosom generasi baru
            """
            print "Generasi ke", generasi + 1
            """
            array_krom1 = array_offspring[0]
            array_krom2 = array_offspring[1]
            array_krom3 = array_offspring[2]
            array_krom4 = array_offspring[3]
            array_krom5 = array_offspring[4]
            array_krom6 = array_offspring[5]
            array_krom7 = array_offspring[6]
            array_krom8 = array_offspring[7]
            array_krom9 = array_offspring[8]
            array_krom10 = array_offspring[9]
            
            # convert ke char        
            char_krom1 = convert_ke_char(char_krom1, array_krom1)
            char_krom2 = convert_ke_char(char_krom2, array_krom2)
            char_krom3 = convert_ke_char(char_krom3, array_krom3)
            char_krom4 = convert_ke_char(char_krom4, array_krom4)
            char_krom5 = convert_ke_char(char_krom5, array_krom5)
            char_krom6 = convert_ke_char(char_krom6, array_krom6)
            char_krom7 = convert_ke_char(char_krom7, array_krom7)
            char_krom8 = convert_ke_char(char_krom8, array_krom8)
            char_krom9 = convert_ke_char(char_krom9, array_krom9)
            char_krom10 = convert_ke_char(char_krom10, array_krom10)
            """
            print "Kromosom1\t", char_krom1
            print "Kromosom2\t", char_krom2
            print "Kromosom3\t", char_krom3
            print "Kromosom4\t", char_krom4
            print "Kromosom5\t", char_krom5
            print "Kromosom6\t", char_krom6
            print "Kromosom7\t", char_krom7
            print "Kromosom8\t", char_krom8
            print "Kromosom9\t", char_krom9
            print "Kromosom10\t", char_krom10, "\n"
            """
            generasi = generasi + 1
        
        output.set(pesan)


# fungsi yang dipasang di button keluar buat close tkinter    
def keluar():
    root.destroy() # close Tkinter
    
def fungsi_objektif(array_krom):
    f_obj = 0
    
    # looping sebanyak gen dalam kromosom
    for q in range (len(array_solusi)):
        
        # fungsi objektif = | array solusi - array kromosom |
        f_obj = f_obj + abs(array_solusi[q]-array_krom[q])
    
    # buat disimpen ke variabel
    return f_obj

def fungsi_fitness(fungsi_obj):
    return 1/(float(fungsi_obj) + 1)
    
def probabilitas(fitness, total):
    return fitness / total

def roulette_wheel(batas1, batas2, batas3, batas4, batas5, batas6, batas7, batas8, batas9, batas10):
    r = random() # fungsi buat random dari 0.0 <= x < 1.0
    
    # belum ada pilihan
    pilihan_roulette = 0
    
    # pemilihan wilayah dalam roulette
    if (batas1 < r and r <= batas2):
        pilihan_roulette = 1
    elif (batas2 < r and r <= batas3):
        pilihan_roulette = 2
    elif (batas3 < r and r <= batas4):
        pilihan_roulette = 3
    elif (batas4 < r and r <= batas5):
        pilihan_roulette = 4
    elif (batas5 < r and r <= batas6):
        pilihan_roulette = 5
    elif (batas6 < r and r <= batas7):
        pilihan_roulette = 6
    elif (batas7 < r and r <= batas8):
        pilihan_roulette = 7
    elif (batas8 < r and r <= batas9):
        pilihan_roulette = 8
    elif (batas9 < r and r <= batas10):
        pilihan_roulette = 9
    else:
        pilihan_roulette = 10
    
    # buat disimpen ke variabel    
    return pilihan_roulette

def rouletted_kromosom(pil, krom1, krom2, krom3, krom4, krom5, krom6, krom7, krom8, krom9, krom10):
    krom_pilihan = []
    if pil == 1:
        krom_pilihan = deepcopy(krom1)
    elif pil == 2:
        krom_pilihan = deepcopy(krom2)
    elif pil == 3:
        krom_pilihan = deepcopy(krom3)
    elif pil == 4:
        krom_pilihan = deepcopy(krom4)
    elif pil == 5:
        krom_pilihan = deepcopy(krom5)
    elif pil == 6:
        krom_pilihan = deepcopy(krom6)
    elif pil == 7:
        krom_pilihan = deepcopy(krom7)
    elif pil == 8:
        krom_pilihan = deepcopy(krom8)
    elif pil == 9:
        krom_pilihan = deepcopy(krom9)
    else:
        krom_pilihan = deepcopy(krom10)
        
    return krom_pilihan

def crossover(kromA, kromB):
    r = randint(1, (len(array_solusi) - 1))
    k = 0
    krom = [0] * len(array_solusi)
    while k < len(array_solusi):
        if k < r:
            krom[k] = kromA[k]
        else:
            krom[k] = kromB[k]
        k = k + 1
    """
    print "Posisi silang offspring:\t", r
    """
    return krom

### DAFTAR FUNGSI - END ###

### DESIGN TKINTER - START ###
    
# bikin frame
frame = Tkinter.Frame(root, width = 500, height = 500)
frame.pack()

# bikin label judul
L1 = Tkinter.Label(frame, text = "Name Generator")
L1.place(y = 20, width = 500, height = 35)

# bikin label jumlah karakter
L2 = Tkinter.Label(frame, text = "Jumlah karakter (2 - 10) :")
L2.place(y = 70, width = 200, height = 35)

# bikin button buat submit jumlah character
input_char = Tkinter.Button(frame, text="input", command = input_char)
input_char.place(x = 375, y = 70, width = 100, height = 40)

# bikin entry buat inputan jumlah character
E2 = Tkinter.Entry(frame)
E2.place(y = 70, x = 250, width = 20, height = 35)

# bikin button keluar
keluar = Tkinter.Button(frame, text="Keluar", command = keluar)
keluar.place(y = 460, width = 500, height = 40)

### DESIGN TKINTER - END ###

### SUPAYA UKURAN WINDOWNYA DI TENGAH - START ###

# buat atur posisi window
w = 500 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

### SUPAYA UKURAN WINDOWNYA DI TENGAH - END ###

# jalanin Tkinter GUI
root.mainloop()