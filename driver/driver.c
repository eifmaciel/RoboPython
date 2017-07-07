#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <asm/uaccess.h>

/*----------------------------------------------------------------------------*/
#define DEVICE 60
#define DEVICE_NAME "robot"
#define BUF_MSG 1

/*----------------------------------------------------------------------------*/
int device_init(void);
void devide_cleanup(void);
static int device_open(struct inode *inode, struct file *file);
static int device_release(struct inode *inode, struct file *file);
static ssize_t device_read(struct file *file, char __user *buffer, size_t length,loff_t * offset);
static ssize_t device_write(struct file *file, const char __user * buffer, size_t length, loff_t * offset);

/*----------------------------------------------------------------------------*/
module_init(device_init);
module_exit(devide_cleanup)

/*----------------------------------------------------------------------------*/
static int is_open = 0;
static char message[BUF_MSG];
static char *ptr;

/*----------------------------------------------------------------------------*/
struct file_operations fops = {
	.read = device_read,
	.write = device_write,
	.open = device_open,
	.release = device_release,
};

/*----------------------------------------------------------------------------*/
int device_init()
{
	int ret;

	ret = register_chrdev(DEVICE, DEVICE_NAME, &fops);

	if (ret < 0) {
		printk("Erro ao carregar o dispositivo %d\n.",DEVICE);
		return ret;
	}

	printk("O dispositivo %d foi carregado.\n", DEVICE);

	return 0;
}

/*----------------------------------------------------------------------------*/
void devide_cleanup()
{
	unregister_chrdev(DEVICE, DEVICE_NAME);
	printk("O dispositivo %d foi descarregado.\n", DEVICE);
}

/*----------------------------------------------------------------------------*/
static int device_open(struct inode *inode, struct file *file)
{
	if (is_open){
		return -EBUSY;
	}
	is_open = 1;
    ptr = message;
	try_module_get(THIS_MODULE);
	printk("O dispositivo %d foi aberto.\n", DEVICE);
	return 0;
}

/*----------------------------------------------------------------------------*/
static int device_release(struct inode *inode, struct file *file)
{
	is_open = 0;
	module_put(THIS_MODULE);
	return 0;
}

/*----------------------------------------------------------------------------*/
static ssize_t device_read(struct file *file, char __user * buffer, size_t length, loff_t * offset){

	int bytes_read = 0;

	if (*ptr == 0){
		return 0;
	}

	while (length && *ptr) {
		put_user(*(ptr++), buffer++);
		length--;
		bytes_read++;
	}
	printk("Leu %d bytes correspondendo a mensagem: %s\n", bytes_read, message);

	return bytes_read;
}

/*----------------------------------------------------------------------------*/
static ssize_t device_write(struct file *file, const char __user * buffer, size_t length, loff_t * offset){

	int i;

	for (i = 0; i < length && i < BUF_MSG; i++){
		get_user(message[i], buffer + i);
	}

	printk("Escreveu a mensagem: %s\n", message);

	ptr = message;

	return i;
}
