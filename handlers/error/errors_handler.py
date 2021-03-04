from loader import dp
from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                      CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter,
                                      CantParseEntities, MessageCantBeDeleted, BotBlocked)
from utils.misc.log import logging


@dp.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, CantDemoteChatCreator):
        logging.debug("Cant Demote Chat Creator")
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('Message Not Modified')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.debug('Message Cant Be Deleted')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug('Message To Delete Not Found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message Text Is Empty')
        return True

    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, BotBlocked):
        logging.warning(f'BotBlocked: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
