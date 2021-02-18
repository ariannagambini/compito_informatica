r=float(input("reddito"))
if r<=15000:
    imposta1=r*23/100
    print("imposta: ", imposta1)
    print("tassazione media: 23%")
else:
    imposta2=(r-15000)

    if imposta2<=28000:
        im1=3450
        im2=imposta2*27/100 
        imposta_tot=im1+im2
        tassazione_media=imposta_tot/r*100
        tm=str(tassazione_media) + "%"
        print("imposta: ", imposta_tot)
        print("tassazione media: ", tm)

    else:
        imposta3=(r-28000)

        if imposta3<=55000:
            im1=3450
            im2=3510
            im3=imposta3*38/100 

            imposta_tot=im1+im2+im3
            tassazione_media=imposta_tot/r*100
            tm=str(tassazione_media) + "%"
            print("imposta: ", imposta_tot)
            print("tassazione media: ", tm)

        else:
            imposta4=(r-55000)
            if imposta4<=75000:
                im1=3450
                im2=3510
                im3=27000*38/100 
                im4=imposta4*41/100
                imposta_tot=im1+im2+im3+im4
                tassazione_media=imposta_tot/r*100
                tm=str(tassazione_media) + "%"
                print("imposta: ", imposta_tot)
                print("tassazione media: ", tm)
            else:
                imposta5=r-75000
                im1=3450
                im2=3510
                im3=27000*38/100 
                im4=20000*41/100
                im5=imposta5*43/100
                imposta_tot=im1+im2+im3+im4+im5
                tassazione_media=imposta_tot/r*100
                tm=str(tassazione_media) + "%"
                print("imposta: ", imposta_tot)
                print("tassazione media: ", tm)

