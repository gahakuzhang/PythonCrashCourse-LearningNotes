#6.3.3 按顺序遍历所有key
#注意sorted的位置
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'a':'maiyan',
    'b':'erika',
    }
for name in sorted(favorite_idols):
    print(name.title()+", thank you for supporting "
          +favorite_idols[name]+"!")

