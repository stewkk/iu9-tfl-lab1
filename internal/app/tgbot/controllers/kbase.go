package controllers

import (
	"errors"
	"fmt"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"

	"github.com/BaldiSlayer/rofl-lab1/internal/app/tgbot/models"
	"github.com/BaldiSlayer/rofl-lab1/internal/app/usecases"
	"github.com/BaldiSlayer/rofl-lab1/internal/version"
)

func (controller *Controller) GetRequest(update tgbotapi.Update) (models.UserState, error) {
	if update.Message == nil {
		return models.GetRequest, nil
	}

	return controller.handleKnowledgeBaseRequest(update)
}

func (controller *Controller) handleKnowledgeBaseRequest(update tgbotapi.Update) (models.UserState, error) {
	answer, err := usecases.AskKnowledgeBase(controller.ModelClient, update.Message.Text)
	if err != nil {
		return 0, err
	}

	return models.GetRequest, errors.Join(
		controller.Bot.SendMessage(
			update.Message.Chat.ID,
			fmt.Sprintf("%s\n\n%s", answer, version.BuildVersion()),
		),
		controller.Bot.SendMessage(
			update.Message.Chat.ID,
			"Введите запрос к Базе Знаний",
		),
	)
}
