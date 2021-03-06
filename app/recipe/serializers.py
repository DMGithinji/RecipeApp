from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_on_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """"Serialize ingredient object"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'ingredients',
                  'tags', 'time_minutes', 'link')
        read_only_fields = ('id',)


class RecipeListSerializer(RecipeSerializer):
    """Serializer for a recipe list view"""
    ingredients = serializers.StringRelatedField(many=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'ingredients',
                  'tags', 'time_minutes', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
