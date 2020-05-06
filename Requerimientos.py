# -*- coding:utf-8 -*-
import csv
import time

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Historial:
    def __init__(self,nombre,telefono,nombre1,telefono1,time1):
        self.nombre = nombre
        self.telefono = telefono
        self.nombre1 = nombre1
        self.telefono1 = telefono1
        self.time1 = time1

class ConctacBook:

    def __init__(self):
        self._contacts = []
        self._histo = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))
        self._save()

    def _addcall(self,nombre,telefono,nombre1,telefono1,time1):
        histo_call = Historial(nombre,telefono,nombre1,telefono1,time1)
        self._histo.append(histo_call)
        print('Emisor: {}, numero emisor: {},r receptor: {}, numero receptor: {}  duracion: {}'.format(nombre,telefono,nombre1,telefono1,time1))
        self._saving_call()

    def show_history(self):
        for histo_call in self._histo:
            self._print_histo(histo_call)

    def _print_histo(self,histo_call):
        print('---*---*---*---*')
        print('Emisor: {}'.format(histo_call.nombre))
        print('Telefono: {}'.format(histo_call.telefono))
        print('Receptor: {}'.format(histo_call.nombre1))
        print('Telefono: {}'.format(histo_call.telefono1))
        print('duracion: {}'.format(histo_call.time1))

    def search_call(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                print('hola {}'.format(contact.name))
                nombre = contact.name
                telefono = contact.phone
                name =str(raw_input('A quien desea llamar? '))
                for contact in self._contacts:
                    if contact.name.lower() == name.lower():
                        nombre1 = contact.name
                        telefono1 = contact.phone
                        print('Llamando a {}'.format(contact.name))
                        starting_point = time.time()
                        print('Estamos llamando....')
                        print('Por favor espere....')
                        print('....')
                        print('Conectado!')
                        time1 = int(time.time()-starting_point)
                        self._addcall(nombre,telefono,nombre1,telefono1,time1)
                        break
                else:
                    self._not_found()
                break
        else:
            self._not_found()

    def _saving_call(self):
        with open('historial_call.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('Emisor', 'Numero emisor','Receptor','numero receptor','duracion'))

            for histo_call in self._histo:
                writer.writerow((histo_call.nombre, histo_call.nombre1, histo_call.nombre1, histo_call.telefono1, histo_call.time1))

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def _not_found(self):
        print('**********')
        print('No encontrado')
        print('************')

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break

        else:
            self._not_found()

    def actualizar(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                contact.name = str(raw_input('Reescribe el nombre del contacto: '))
                contact.phone = str(raw_input('Reescribe el telefono del contacto: '))
                contact.email = str(raw_input('Reescribe el email del contacto: '))
                break
                self._save()
        else:
            self._not_found()

    def _save(self):
        with open('abonados.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('---*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))

    def show_names(self):
        i=0
        for contact in self._contacts:
            print('[{}] {}'.format(i,contact.name))

def run():
    contact_book = ConctacBook()
    with open('abonados.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    with open('historial_call.csv', 'r') as f:
        lector = csv.reader(f)
        for idx, row in enumerate(lector):
            if idx == 0:
                continue
            contact_book._addcall(row[0], row[1], row[2],row[3],row[4])
    while True:
        command = str(raw_input('''
        Qué desea hacer? 
        
        [ll]lamar a un abonado
        [h]istorial de llamadas 
        [a]ñadir un abonado 
        [ac]tualizar abonados
        [b]uscar abonados
        [e]liminar un abonado
        [l]istar abonados
        [s]alir 
        '''))


        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)

        elif command == 'h':
            contact_book.show_history()

        elif command == 'll':
            name = str(raw_input('Identifiquese con su nombre completo: '))
            contact_book.search_call(name)



        elif command == 'ac':
            name = str(raw_input('Escribe el nombre del a actualizar: '))
            contact_book.actualizar(name)

        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)
            print('buscar contacto')

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)


        elif command == 'l':
            contact_book.show_all()


        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A L  I N T E R C O M U N I C A D O R ')
    run()