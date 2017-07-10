# RoboPython

# Criar os arquivos do driver
    make

# Criando o arquivo e carregando o módulo
    sudo mknod /dev/robo c 60 0
    sudo chmod 666 /dev/robo
    sudo insmod driver.ko

# Testando o módulo
    echo "r" > /dev/robo
    cat /dev/robo

# Removendo o módulo e o arquivo
    sudo rmmod driver.ko
    sudo rm /dev/robo

# Startando a aplicação
    python2.7 mainTeclado.py
    python2.7 mainRobo.py
