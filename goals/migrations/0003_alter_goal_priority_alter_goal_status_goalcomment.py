from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("goals", "0002_goal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goal",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Низкий"),
                    (2, "Средний"),
                    (3, "Высокий"),
                    (4, "Критический"),
                ],
                default=2,
                verbose_name="Приоритет",
            ),
        ),
        migrations.AlterField(
            model_name="goal",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "К выполнению"),
                    (2, "В процессе"),
                    (3, "Выполнено"),
                    (4, "Архив"),
                ],
                default=1,
                verbose_name="Статус",
            ),
        ),
        migrations.CreateModel(
            name="GoalComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(verbose_name="Дата создания")),
                (
                    "updated",
                    models.DateTimeField(verbose_name="Дата последнего обновления"),
                ),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "goal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="goal_comments",
                        to="goals.goal",
                        verbose_name="Цель",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="goal_comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий к цели",
                "verbose_name_plural": "Комментарии к целям",
            },
        ),
    ]
