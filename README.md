# OvisApp: ПО для анализа вязкости нефти

Настоящая программа использует машинное обучение для предсказания вязкости нефти и температуры её структурного фазового перехода.

## Установка в Windows

1. Установите [Anaconda](https://www.anaconda.com/download/success).

2. Запустите установившуюся программу *Anaconda Powershell Prompt*.

3. Создайте новое окружение:

```bash
> conda create -n ovis python=3.10 pip
```

Здесь "ovis" - имя окружение, его можно менять на любое другое.

4. Активируйте созданное окружение:

```bash
> conda activate ovis
```

5. Скачайте с GitHub'а архив с программой (зелёная кнопка "Code", среди вариантов выбрать "Download ZIP").

6. Распакуйте архив в удобном месте, например, сразу в папке "Загрузки".

7. В открытой консоли (программа *Anaconda Powershell Prompt*) смените текущую директорию на папку со скачанным ПО:

```bash
> cd C:\Users\TheBestUser\Downloads\OvisApp-main
```

Здесь вместо TheBestUser нужно подставить актуальное имя пользователя.

8. Установите программы следующей коммандой:

```bash
> pip install ./
```

9. Если не появилось сообщений об ошибках, то поздравляем, программа установлена!


## Запуск ПО в Windows

### Долгий путь

1. Запустите *Anaconda Powershell Prompt*.

2. Активируйте окружение с установленной программой:

```bash
> conda activate ovis
```

3. Запустите программу следующей командой:

```bash
> python -m ovis
```

4. Для остановки программы требуется нажать `Ctrl+C` в консоли или закрыть окно консоли.


### Быстрый путь

1. Скачайте файл [ovis.bat](misc/ovis.bat) из папки [misc](misc/) и переместите в удобную локацию.

2. Откройте его с помощью текстового редактора (например, щелчок правой кнопкой мыши и "Открыть в Notepad").

3. Во второй и третьей строчках файла замените путь к установленной Anaconda (`set root=...`) и имя окружения conda  (`set env=...`) на актуальные значения.

4. Теперь двойной щелчок по файлу будет запускать программу в новом окне или новой вкладке браузера по умолчанию.

5. Для закрытия программы требуется закрыть появляющуюся вместе с программой окно консоли.

