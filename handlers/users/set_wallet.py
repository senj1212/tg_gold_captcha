from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from database import get_user_by_uid, set_user_wallet
from loader import dp, bot
from lang import get_translation
from keyboards.inline import ikb_set_wallet_menu, ikb_btn_menu
from aiogram.types import CallbackQuery, Message
from core import is_valid_payeer_wallet


class WalletSet(StatesGroup):
    wallet = State()


@dp.callback_query_handler(text="set_wallet")
async def callback_set_wallet_menu(call: CallbackQuery):
    language = call.from_user.language_code
    await WalletSet.wallet.set()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    await bot.send_message(call.from_user.id,
                           text=get_translation(language, "specify_wallet"),
                           reply_markup=ikb_set_wallet_menu(language))


@dp.callback_query_handler(text="accept_wallet", state=WalletSet.wallet)
async def callback_set_wallet_menu(call: CallbackQuery, state: FSMContext):
    language = call.from_user.language_code
    user = await get_user_by_uid(call.from_user.id)

    if user.wallet != "":
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await state.finish()
        await bot.send_message(call.from_user.id,
                               text=get_translation(language, "great_wallet"),
                               reply_markup=ikb_btn_menu(language))
    else:
        await bot.answer_callback_query(call.id, text=get_translation(language, "bad_wallet"), show_alert=True)


@dp.message_handler(content_types=['text'], state=WalletSet.wallet)
async def set_wallet_state(message: Message, state: FSMContext):
    if is_valid_payeer_wallet(message.text):
        await set_user_wallet(message.from_user.id, message.text)
    else:
        await set_user_wallet(message.from_user.id, "")
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
