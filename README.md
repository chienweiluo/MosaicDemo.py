# SimpleMosaicDemo.py

simple mosaic application by python.

### core

    def mosaic():
    path = entry.get()

    im = Image.open(""+path)
    im.show()
    newim= im

    def avg_clr(p):
            c = list(p.getdata())
            b = len(c)
            k = list(map(sum,zip(*c)))
            q = (int(k[0]/b),int(k[1]/b),int(k[2]/b))
            return q

    def divide(w,h,s):
            global newim
            newim= im
            boxes = [(x,y,x+s,y+s) for x in range(0,w,s) for y in range(0,h,s)]
            for box in boxes:
                snip = newim.crop(box)
                im.paste(avg_clr(snip),box)
                
    def main():
            divide(newim.size[0],newim.size[1],20)
            newim.show()
            newim.save("mosaicout.png")

    main()
