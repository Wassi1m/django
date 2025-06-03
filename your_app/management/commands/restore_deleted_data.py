from django.core.management.base import BaseCommand
from django.core import serializers
import json
from your_app.models import * # Remplacez par vos modèles spécifiques

class Command(BaseCommand):
    help = 'Restaure les données supprimées en se basant sur les IDs connus'

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # Charger le fichier fixture
        with open('your_app/fixtures/backup_data.json', 'r') as fixture_file:
            backup_data = json.load(fixture_file)

        # Les IDs que vous connaissez qui ont été supprimés
        deleted_ids = options['ids']
        
        # Dictionnaire pour suivre les objets à restaurer
        to_restore = {}
        
        # Première passe : identifier les objets directement liés aux IDs supprimés
        for item in backup_data:
            model = item['model']
            if item['pk'] in deleted_ids:
                if model not in to_restore:
                    to_restore[model] = set()
                to_restore[model].add(item['pk'])

        # Deuxième passe : trouver les objets liés
        changed = True
        while changed:
            changed = False
            for item in backup_data:
                model = item['model']
                fields = item['fields']
                
                # Vérifier si cet objet fait référence à un objet à restaurer
                for field, value in fields.items():
                    if isinstance(value, int) and any(value in to_restore.get(m, set()) for m in to_restore):
                        if model not in to_restore:
                            to_restore[model] = set()
                        if item['pk'] not in to_restore[model]:
                            to_restore[model].add(item['pk'])
                            changed = True
                            
        # Restaurer les objets
        for item in backup_data:
            model = item['model']
            if model in to_restore and item['pk'] in to_restore[model]:
                try:
                    # Désérialiser et sauvegarder l'objet
                    for obj in serializers.deserialize('json', json.dumps([item])):
                        obj.save()
                    self.stdout.write(self.style.SUCCESS(f'Restauré {model} avec ID {item["pk"]}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Erreur lors de la restauration de {model} {item["pk"]}: {str(e)}')) 