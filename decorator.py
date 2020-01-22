def param_decor(log_path):

    def decorate_foo(people):
        def decorate_around_people(*args, **kwargs):
            logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                                format='%(asctime)s - %(funcName)s - %(message)s')
            logging.info(f'Функция стартовала ')
            result = people(*args, **kwargs)
            logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                                format='%(asctime)s - %(message)s')
            logging.info(f'Функция завершила работу')
            path_of_log = os.path.abspath('Simplelog.log')
            logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                                format='%(asctime)s - %(message)s')
            logging.info(f'Путь к файлу {path_of_log}')
            logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                                format=f'%(asctime)s - %(message)s')
            logging.info(f'Функция вернула {result}')
            return result
        return decorate_around_people
    return decorate_foo