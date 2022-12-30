
@client.command(brief="<probability> <number of trials to success>")
async def geometric(ctx, p, n):
    await ctx.send(float(p)*sum([(1-float(p))**x for x in range(int(n))]))

@client.command(brief = "<no of runs until and INCLUDING the trial when you got the drop> <''> <''> ...",description="Please call this command together with all number of times you had to run in order to get your drop in question. The more times you have to provide for me to study, the better :D")
async def Droprate(ctx, s, n):
    s = int(s)
    n = int(n)
    p1 = s/n
    p2 = (s-1)/(n-1)
    await ctx.send(f'`` mle/mme estimate of drop rate with given input is {p1*100}% ``')
    await ctx.send(f'`` minimum variance unbiased estimator (mvue) estimate of drop rate with given input is {p2*100}% ``')
    conf = [.5,.75,.90]
    end = []
    end2 = []
    for i in conf:
        end.append(np.log(1-i)/np.log(1-p1))
        end2.append(np.log(1-i)/np.log(1-p2))
    await ctx.send('B⃞    e⃞    e⃞    p⃞     b⃞    o⃞    o⃞    p⃞')
    for i in range(len(end)):
        await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end[i])} runs :D - according to mme/mle prob =3=  ``')
        try:
            await ctx.send(f'`` {conf[i]*100}% confidence that you will get a drop in {math.ceil(end2[i])} runs :D - according to mvue prob ``')
        except:
            pass